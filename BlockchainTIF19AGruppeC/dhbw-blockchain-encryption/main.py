import base64
import io
import json
import pathlib
import requests
from base64 import encodebytes
from collections import Counter

from PIL import Image
from ecies import decrypt
from flask import Flask, request, jsonify, make_response

from auth_service import user_authenticated, get_server_from_discovery_service, add_private_key, save_admin_keys, \
    get_admin_priv_key, get_priv_keys, get_admin_pub_key
from encryption_service import submit_vote_to_blockchain, private_key_list, generate_admin_private_key
from config_management import get_options, is_election_over, has_election_started

app = Flask(__name__)


def get_response_image(voting_image_path):
    pil_img = Image.open(voting_image_path, mode='r')
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG')
    encoded_img = encodebytes(byte_arr.getvalue()).decode('UTF-8')
    return encoded_img


def remove_file(image_path):
    file = pathlib.Path(image_path)
    file.unlink()


# INITIAL RUN REQUIREMENT:
#if admin key is empty in database
#(admin_pub_key, admin_priv_key) = generate_admin_private_key()
#save_admin_keys(admin_pub_key, admin_priv_key)
admin_priv_key = get_admin_priv_key()
admin_pub_key = get_admin_pub_key()

@app.route('/api/getOptions', methods=['POST'])
def return_options():
    response = prepare_response(jsonify(get_options()), 200)
    return response

@app.route('/api/transmit', methods=['POST'])
def create_record():
    personal_number = request.form['personal_number']
    pin = request.form['pin']
    auth_pin = request.form['auth_pin']
    partei = request.form['partei']

    if (not has_election_started()):
        response = prepare_response(jsonify(
            {"status": "error",
             "description": "Election has not started"}), 403) #403 = HTTP Access Forbidden code
        return response

    if is_election_over():
        response = prepare_response(jsonify(
            {"status": "error",
             "description": "Election has ended"}), 403) #403 = HTTP Access Forbidden code
        return response

    if user_authenticated(personal_number, auth_pin):
        registered_vote = submit_vote_to_blockchain(
                                personal_number=personal_number,
                                pin=pin,
                                vote_party=partei)
        if registered_vote is not None:
            voter_number = registered_vote[0]
            voter_private_key = registered_vote[2]
            send_vote(registered_vote[0], registered_vote[1])

            public_image_path = 'public_' + personal_number + '.png'
            private_image_path = 'private_' + personal_number + '.png'
            voter_image_path = 'personal_' + personal_number + '.png'

            encoded_public_key = get_response_image(public_image_path)
            encoded_private_key = get_response_image(private_image_path)
            encoded_voter_key = get_response_image(voter_image_path)

            remove_file(public_image_path)
            remove_file(private_image_path)
            remove_file(voter_image_path)

            #Replace use of private_key_list (global variable) with return value
            #add_private_key(voter_number, private_key_list[0], admin_pub_key)
            add_private_key(voter_number, voter_private_key, admin_pub_key)

            response = prepare_response(jsonify({
                'status': 'success',
                'voter_id': voter_number,
                'PublicImageBytes': encoded_public_key,
                'PrivateImageBytes': encoded_private_key,
                'VoterImageBytes': encoded_voter_key
            }), 201)
            return response
    else:
        response = prepare_response(jsonify({
            'status': 'auth-error',
            'reason': "Falscher Auth-Code",
        }), 401)
        return response

    response = prepare_response(jsonify({
        'status': 'error',
        'reason': "Sie haben bereits abgestimmt.",
    }), 400)
    return response


def prepare_response(json, code):
    response = make_response(json, code)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


@app.route('/api/getAuszaehlung', methods=['POST'])
def get_auszaehlung():
    #First check if the elections is over and we can send the tally
    if not is_election_over():
        response = prepare_response(jsonify(
            {"status": "error",
             "description": "Election still in progress"}), 403) #403 = HTTP Access Forbidden code
        return response
    
    #Initialize empty result dictionary
    results = {}
    #Initialize it with the options from the config file
    for option in get_options():
        results[option] = 0 

    r = requests.post("http://127.0.0.1:45675/api/getTransactions")
    transactions = r.json()

    voted = []

    for transaction in transactions:
        personal_number = transaction['voter_id']
        if personal_number in voted:
            continue
        else:
            voted.append(personal_number)

        encrypted_user_key = get_priv_keys(personal_number)
        user_key = base64.b64decode(encrypted_user_key)
        private_key = decrypt(admin_priv_key, user_key)

        encrypted_vote_base64 = str(transaction['encrypted_vote'])
        encrypted_vote = base64.b64decode(encrypted_vote_base64)
        output = decrypt(private_key.decode('UTF-8'), encrypted_vote)
        
        #Skip unknown values for now
        vote = output.decode('UTF-8')
        print("Decrypted vote: " + vote)
        if vote not in get_options():
            #NOTE: This would be a great place to implement write-in ballots
            #Only some additional update logic would be needed here
            continue
        else:
            results[vote] += 1;

    response_dict = {"status": "success", "results": results}
    #print(response_dict)
    response = prepare_response(jsonify(response_dict), 200)
    return response


@app.route('/api/receive', methods=['POST'])
def receive_vote():
    content = request.json
    layers_left = content['layers_left']
    hashed_personal_number = content['hashed_personal_number']
    encrypted_vote = content['encrypted_vote']
    decreased_layers = int(layers_left) - 1

    if decreased_layers == 0:
        send_layers_request("http://127.0.0.1:45675/api/commitVote",
                            decreased_layers, hashed_personal_number, encrypted_vote)
        return jsonify({
            'status': 'written'
        }), 200
    else:
        layers_left = decreased_layers
        url = get_server_from_discovery_service()
        send_layers_request(url, layers_left, hashed_personal_number, encrypted_vote)
        return jsonify({
            'status': 'written',
            'layers_left': layers_left
        }), 200


def send_layers_request(url, layers, hashed_personal_number, encrypted_vote):
    data = {'layers_left': str(layers),
            'hashed_personal_number': hashed_personal_number,
            'encrypted_vote': encrypted_vote}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)


def send_vote(hashed_personal_number, encrypted_vote):
    layers = 3
    url = get_server_from_discovery_service()
    send_layers_request(url, layers, hashed_personal_number, encrypted_vote)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=45677, debug=True)
