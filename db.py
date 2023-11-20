# db.py

import sqlite3
from flask import Flask, g

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            schema = f.read()
        db.executescript(schema)
        db.commit()

def create_tables():
    # Define your create_tables logic here
    pass

def register_user(username, password):
    with get_db() as db:
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        db.commit()

def get_user_by_username(username):
    with get_db() as db:
        cursor = db.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user

def check_password(username, password):
    user = get_user_by_username(username)
    print(f"User: {user}")  # Add this line for debugging
    if user is not None:
        # Check the stored password against the provided password (plaintext comparison)
        stored_password = user['password']
        return stored_password == password
    return False

if __name__ == '__main__':
    init_db(app)
