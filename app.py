from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import init_db, register_user, get_user_by_username, check_password

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Initialize the database
init_db(app)

# Additional routes and configurations go here...
# For example, a simple home route:

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            message = 'Both username and password are required'
        elif get_user_by_username(username) is not None:
            message = 'Username already taken'
        else:
            register_user(username, password)
            message = 'Registration successful'

    return render_template('register.html', message=message)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if user and check_password(username, password):
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            message = 'Incorrect username or password'

    return render_template('login.html', message=message)

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

# Route to handle poll1 submissions
@app.route('/poll1', methods=['GET', 'POST'])
def poll1():
    if 'username' not in session or not session['logged_in']:
        flash('You must be logged in to submit polls.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        favorite_game = request.form.get('favorite_game')
        # Process the submission as needed
        flash(f'Thank you for submitting your favorite game: {favorite_game}', 'success')

    return render_template('poll1.html')

# Route to handle poll2 submissions
@app.route('/poll2', methods=['GET', 'POST'])
def poll2():
    if 'username' not in session or not session['logged_in']:
        flash('You must be logged in to submit polls.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        disappointing_game = request.form.get('disappointing_game')
        # Process the submission as needed
        flash(f'Thank you for submitting the most disappointing game: {disappointing_game}', 'success')

    return render_template('poll2.html')

if __name__ == '__main__':
    app.run(debug=True)
