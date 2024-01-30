# Do not modify these lines
__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

# Add your code after this line
'''
flask-group:
1. authentication
2. requests
3. templates
'''

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Home, sweet home.</p>', 200

'''
imho: the comma converts the returned value into a tuple. 
'''

@app.route('/greet')
def greet():
    return '<h1>Hello, world!</h1>', 200

@app.route('/greet/<name>')
def greet_name(name):
    return f'<h1>Hello, {name}!</h1>', 200

if __name__ == '__main__':
    app.run()

'''
pitfall: if I omit '200' (i.e. the response.status_code)
then the test will still succeed. But why? 

'''





