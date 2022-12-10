import random
import mariadb

from auth_service import save_admin_keys
from encryption_service import generate_admin_private_key
from config_management import get_voter_count

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_connection():
    new_connection = mariadb.connect(
                user="root",
                password="Gu3487#2399!!+dj8v83bnd",
                host="127.0.0.1",
                port=3306,
                database="auth_register")
    return new_connection

conn = get_connection()
cur = conn.cursor()
voter_count = get_voter_count()
#Clear tables
cur.execute("TRUNCATE TABLE voters")
cur.execute("TRUNCATE TABLE directory_server3")
conn.commit()
#Generate admin key
(admin_pub_key, admin_priv_key) = generate_admin_private_key()
save_admin_keys(admin_pub_key, admin_priv_key)
#Generate information for each voter
voter_info = []
for i in range(voter_count):
    letter_part = random.choice(alphabet)
    number_part = f"{random.randint(0, 999999999):09}"
    personal_id = letter_part + number_part
    
    auth_id = random.randint(100000, 999999)
    
    voter_info.append((personal_id, 0, auth_id))

sql_query = "INSERT INTO voters (PERSON_ID, HAS_VOTED, AUTH_ID) VALUES (?, ?, ?)"
cur.executemany(sql_query, voter_info)
conn.commit()
conn.close()
print(f"Setup completed for new election ({voter_count} voters).")
    