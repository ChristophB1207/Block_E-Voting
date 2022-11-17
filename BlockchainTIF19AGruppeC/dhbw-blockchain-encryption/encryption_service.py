import base64
import qrcode
import argon2
from ecies import encrypt
from ecies.utils import generate_eth_key
import gc

from auth_service import can_user_vote, vote_user


def hash_person_id(personal_number, pin):
    argon_hash = argon2.hash_password(str.encode(personal_number + pin),
                                      memory_cost=2 ** 15, time_cost=16, parallelism=2, hash_len=32,
                                      salt=str.encode(pin + pin))
    return argon_hash.decode()


def create_qr_code(key, key_type, personal_number):
    qr = qrcode.QRCode()
    qr.add_data(key)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(key_type + "_" + personal_number + ".png")


def save_public_and_private_key(public_key, private_key, personal_number):
    create_qr_code(public_key, "public", personal_number)
    create_qr_code(private_key, "private", personal_number)
    del private_key
    del public_key
    gc.collect()


def save_personal_hash(personal_hash, personal_number):
    create_qr_code(personal_hash, "personal", personal_number)


private_key_list = []


def submit_vote_to_blockchain(personal_number, pin, vote_party):
    if not can_user_vote(personal_number):
        return None

    personal_hash = hash_person_id(personal_number, pin)
    (public_key, private_key, encrypted_vote) = encrypt_vote(vote_party)
    save_public_and_private_key(public_key, private_key, personal_number)
    #This is probably not threadsafe
    #private_key_list.clear()
    #private_key_list.append(private_key)
    save_personal_hash(personal_hash, personal_number)

    base64_vote = base64.b64encode(encrypted_vote)
    vote_user(personal_number)
    #Pass the private key over the return value instead of a global variable
    return [personal_hash, base64_vote.decode(), private_key]


def encrypt_vote(vote) -> (str, str, str):
    priv_key = generate_eth_key()

    private_key_hex = priv_key.to_hex()
    public_key_hex = priv_key.public_key.to_hex()
    output = encrypt(public_key_hex, vote.encode())
    return public_key_hex, private_key_hex, output


def generate_admin_private_key():
    admin_priv_key = generate_eth_key()
    admin_priv_key_hex = admin_priv_key.to_hex()
    admin_public_key_hex = admin_priv_key.public_key.to_hex()
    return admin_public_key_hex, admin_priv_key_hex
