

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

'''
flask-group:
1. authentication
2. requests
3. templates
'''

'''
import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    # YOUR SOLUTION HERE
    pass


@app.route("/dashboard")
def dashboard():
    # YOUR SOLUTION HERE
    pass


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    pass
'''

# inspiration:
# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask

import os

from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import get_users, hash_password

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


'''
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username'] 
        data = get_users()
        username = request.form.get('username')
        password = request.form.get('password')
        if username in data:
            user = data[username] 
            if user == hash_password(password):
                return redirect(url_for('dashboard'))
            else:
                redirect(url_for('login', error=True))
                flash('Password is wrong')
        else:
            redirect(url_for('login', error=True))
            flash('Username is wrong')
    return render_template('login.html')
'''
    

# 2do: update code above into code below: (read info in doc pyt_slack_cases to understand the differences)
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        data = get_users()
        username = request.form.get('username') # knoledge of pyt flask forms required. 
        password = request.form.get('password')
        if username in data:
            user = data[username] # mocks / simulates oauth: on server retrieving user's hashed password from database
            if user == hash_password(password):  # mocks / simulates oauth: on local machine hashing user's password
                session['username'] = request.form['username'] # knowledge of session obj required. 
                return redirect(url_for('dashboard')) # pitfall: you must return the redirect fn call.
            else:
                flash('Password is wrong') # knowledge of flash messages required. 
                return redirect(url_for('login', error=True))
 
        else:
            flash('Username is wrong')
            return redirect(url_for('login', error=True))
            
    elif request.method == 'GET': # anticipate on user's erroneous GET request
        return render_template('login.html')



@app.route("/dashboard")
def dashboard():
    try:
        active_user = session['username']
    except (KeyError, TypeError):
        return redirect(url_for('index'))
    return render_template("dashboard.html", title="Dashboard", active_user=active_user)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None) # knowledge of session obj required. 
    return redirect(url_for('index'))






