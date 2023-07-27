# importing the `Flask` class
from flask import (
    abort,
    Flask,
    make_response,
    redirect,
    request
)

# creating flask application instance
app = Flask(__name__)

# root URL for the application
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# static url with a dynamic component
def user(name):
    return f'<h1>Hello {name}!</h1>'

# routing using method
app.add_url_rule('/user/<name>','user',user)

# Accessing the request objects throguh the request context
@app.route('/context/')
def context():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Your Browser is {user_agent}</h1>'

@app.route('/response/')
def response():
    # making response using the response object
    response = make_response('<h1>testing request</h1>')
    response.status_code = 400
    return response

@app.route('/redirect/')
def new():
    return redirect('http://example.com')

@app.route('/id/<int:id>')
def get_id(id):
    if id != 10:
        abort(400)
    response = make_response('<h1>Welcome</h1>')
    return response