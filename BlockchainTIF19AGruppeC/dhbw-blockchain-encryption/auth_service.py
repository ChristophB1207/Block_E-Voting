import base64
import random
from ecies import encrypt
import mariadb

def get_connection():
    conn = mariadb.connect(
                user="root",
                password="Gu3487#2399!!+dj8v83bnd",
                host="127.0.0.1",
                port=3306,
                database="auth_register")
    return conn

def get_admin_priv_key():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin_key_server WHERE server_Id = ?;", ("default",))
    for (id, server_Id, pub_key, priv_key) in cur:
        conn.close()
        return priv_key


def get_admin_pub_key():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin_key_server WHERE server_Id = ?;", ("default",))
    for (id, server_Id, pub_key, priv_key) in cur:
        conn.close()
        return pub_key


def get_priv_keys(personal_ID):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM directory_server3 WHERE personal_ID = ? ;", (personal_ID, ))
    for (id, personal_ID, priv_key) in cur:
        conn.close()
        return priv_key


def save_admin_keys(pub_key, priv_key):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE admin_key_server SET pub_key = ?, priv_key = ? WHERE server_Id = ?;", (pub_key,priv_key,"default"))
    conn.commit()
    conn.close()


def add_private_key(personal_number,  private_key, admin_public_key):
    conn = get_connection()
    cur = conn.cursor()
    encrypted_private_key = base64.b64encode(encrypt(admin_public_key, private_key.encode()))
    cur.execute("INSERT INTO directory_server3 (personal_ID, priv_key) VALUES (?, ?);", (personal_number, encrypted_private_key))
    conn.commit()
    conn.close()


def user_authenticated(person_id, auth_code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM voters WHERE PERSON_ID = ?;", (person_id,))

    for (id, PERSON_ID, HAS_VOTED, AUTH_ID) in cur:
        conn.close()
        return AUTH_ID == int(auth_code)


def vote_user(person_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE voters SET HAS_VOTED = 1 WHERE PERSON_ID = ?;", (person_id,))
    conn.commit()
    conn.close()


def reset_vote(person_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE voters SET HAS_VOTED = 0 WHERE PERSON_ID = ?;", (person_id,))
    conn.commit()
    conn.close()


def can_user_vote(person_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM voters WHERE PERSON_ID = ?;", (person_id,))

    for (id, PERSON_ID, HAS_VOTED, AUTH_ID) in cur:
        conn.close()
        return HAS_VOTED == 0


def get_server_from_discovery_service():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM server;")

    server_ips = []
    for (id, server_name, server_ip, server_port) in cur:
        server_ips.append("http://" + str(server_ip) + ":" + str(server_port) + "/api/receive")
    conn.close()
    return random.choice(server_ips)
