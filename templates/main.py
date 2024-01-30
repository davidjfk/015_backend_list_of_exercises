__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

'''

flask-group:
1. authentication
2. requests
3. templates

read this first:
Why does ' py .\main.py' not work to start Flask application?

The following does work to start Flask application:
    $env:FLASK_APP = "main"
    $env:FLASK_DEBUG = "1"
    flask run --port 5000


'''

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
'''
pitfall: do not create a fn to show base.html
'''

'''
@app.route("/")
def index():
    return "This is an empty Flask project that you need to work on."
'''

@app.route("/", methods= ["GET"])
def index():    
    return render_template("index.html", title="Index")

@app.route("/home", methods= ["GET"])
def home():
    return redirect("/", code=302) # keeps the code DRY.

'''
pitfall: home page is also extending base.html. In other words:
home page is NOT the "base page" to extend from.
'''

@app.route("/about", methods= ["GET"])
def about():
    return render_template("about.html", title="About")

@app.route("/poem", methods= ["GET"])
def fullstack_dev_poem():
    return render_template("fullstack_dev_poem.html", title="fullstack dev poem")