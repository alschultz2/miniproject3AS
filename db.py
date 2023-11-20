import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = 'site.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    with open('schema.sql', 'r') as schema_file:
        schema = schema_file.read()
        cursor.executescript(schema)
    conn.commit()
    conn.close()

def register_user(username, password):
    password_hash = generate_password_hash(password, method='sha256')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def check_password(user, password):
    return user and check_password_hash(user[2], password)