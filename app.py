# importing the `Flask` class
from flask import Flask

# creating flask application instance
app = Flask(__name__)

# root URL for the application
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# static url with a dynamic component
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}!</h1>'