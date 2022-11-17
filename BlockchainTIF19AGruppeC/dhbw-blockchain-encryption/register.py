import base64
import copy
import io
import json
import random
import pathlib

from PIL import Image
from ecies import decrypt
from flask import Flask, request, jsonify, make_response, Response
from pyzbar import pyzbar

from blockchain import BlockChain


app = Flask(__name__)

chain = BlockChain(app)


@app.route('/api/commitVote', methods=['POST'])
def commit_vote():
    content = request.json
    hashed_personal_number = content['hashed_personal_number']
    encrypted_vote = content['encrypted_vote']
    chain.append([hashed_personal_number, encrypted_vote])
    print(chain.__str__())
    return jsonify({'status': 'written'}), 200

#Return the transactions on the chain (for tallying)
@app.route('/api/getTransactions', methods=['POST'])
def get_transactions():
    blocks = []
    blockss = copy.copy(chain)
    for block in blockss.blocks[1:]:
        voter_id = block.transactions[0].replace('\'', '') #Why? There shouldn't be any backslashes in the transactions
        encrypted_vote = block.transactions[1].replace('\'', '')
        blocks.append({'voter_id': voter_id, 'encrypted_vote': encrypted_vote})
    return Response(json.dumps(blocks), mimetype='application/json'), 200

#Return the full blockchain for external verification
@app.route('/api/getFullChain', methods=['POST'])
def get_full_chain():
    blocks = []
    blockss = copy.copy(chain)
    for block in blockss.blocks[0:]:
        voter_id = block.transactions[0].replace('\'', '')
        encrypted_vote = block.transactions[1].replace('\'', '')
        blocks.append({'block_nr': block.nr,
                       'voter_id': voter_id,
                       'encrypted_vote': encrypted_vote,
                       'hash_before': block.hash_before,
                       'hash': block.hash})
    response = prepare_response(json.dumps(blocks), 200)
    return response
    #return Response(json.dumps(blocks), mimetype='application/json'), 200


def get_encrypted_vote(hashed_personal_number):
    for i in range(len(chain.blocks)):
        if chain.blocks[i].transactions[0] == hashed_personal_number:
            return chain.blocks[i].transactions[1]


def decode_qr(image):
    file_name = 'test' + str(random.randint(2, 600000)) + '.jpeg'
    img = Image.open(io.BytesIO(image))
    img.save(file_name, 'jpeg')
    qr = pyzbar.decode(Image.open(file_name))

    file = pathlib.Path(file_name)
    file.unlink()
    return qr[0].data.decode('UTF-8')


def prepare_response(json, code):
    response = make_response(json, code)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def decrypt_vote(encrypted_vote, private_key):
    try:
        encrypted_vote = base64.b64decode(encrypted_vote)
        output = decrypt(private_key, encrypted_vote)
        return output.decode("utf-8")
    except TypeError:
        return None


@app.route('/api/getVote', methods=['POST'])
def get_vote():
    qr_hashed_personal_number = request.form['personal_id_qr_base64'][22:]
    qr_private_key = request.form['private_key_qr_base64'][22:]

    image = base64.b64decode(qr_hashed_personal_number)
    hashed_personal_number = decode_qr(image)

    image2 = base64.b64decode(qr_private_key)
    private_key = decode_qr(image2)

    encrypted_vote = get_encrypted_vote(hashed_personal_number)

    if encrypted_vote is None:
        response = prepare_response(jsonify({
            'status': 'error',
            'reason': "Wahleintrag wurde nicht gefunden.",
        }), 404)
        return response

    voted_party = decrypt_vote(encrypted_vote, private_key)

    if voted_party is None:
        response = prepare_response(jsonify({
            'status': 'error',
            'reason': 'Fehler beim Entschlüsseln.',
        }), 501)
        return response

    response = prepare_response(jsonify({
        'status': 'success',
        'hashedPersonalId': hashed_personal_number,
        'votedParty': voted_party,
    }), 200)
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=45675, debug=True)
