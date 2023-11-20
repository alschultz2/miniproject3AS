from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import create_tables, register_user, get_user_by_username, check_password

app = Flask(__name__)
app.secret_key = 'your-secret-key'

create_tables()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registration logic
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
