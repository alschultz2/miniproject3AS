# INF601 - Advanced Programming in Python
# Adam Schultz
# Mini Project 3

# (5/5 points) Initial comments with your name, class and project at the top of your .py file. Completed
# (5/5 points) Proper import of packages used. Completed
# (70/70 points) Using Flask you need to setup the following: Completed
# 10/10 points) Setup a proper folder structure, use the tutorial as an example. Completed
# (20/20 points) You need to have a minimum of 5 pages, using a proper template structure. Completed(2 are only accessable after loging in).
# (10/10 points) You need to have at least one page that utilizes a form and has the proper GET and POST routes setup. Completed
# (10/10 points) You need to setup a SQLlite database with a minimum of two tables, linked with a foreign key. Maybe.....
# (10/10) You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but
# the more practice here the better. You need to at least make use of a modal. Completed
# (10/10) You need to setup some sort of register and login system, you can use the tutorial as an example. Completed
# (5/5 points) There should be a minimum of 5 commits on your project, be sure to commit often! Completed
# (5/5 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file
# which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt. Completed
# (10/10 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements,
# and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. You will need to explain
# the steps of initializing the database and then how to run the development server for your project.

from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import init_db, register_user, get_user_by_username, check_password
# Above are all the imports for the project

app = Flask(__name__)
app.secret_key = '318725'
# Above is the flask initializations and the secret key ....shhhhhhhhhh.

init_db(app)
# Above initializes the database


@app.route('/')
def home():
    return render_template('home.html')
# Above is the home route


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
# Above is the register route


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
# Above is the login route


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))
# Above deals with the logout part of the program


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
# Everything above deals with connecting the route to poll1


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
# Everything above deals with connecting to the route of poll2


if __name__ == '__main__':
    app.run(debug=True)
#Makes sure that the program doesnt run imported as a module but when a script is executed.
