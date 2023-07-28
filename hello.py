# importing the `Flask` class
from datetime import datetime
from flask import (
    abort,
    Flask,
    make_response,
    redirect,
    render_template,
    request
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# creating flask application instance
# and initializing flask extensions
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# root URL
@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    return response

# user URL
@app.route('/user/<name>')
def user(name):
    response = make_response(render_template('user.html',name=name))
    return response

@app.route('/datetime/')
def date_time():
    response = make_response(render_template('date.html', current_time=datetime.utcnow()))
    return response

# error handling views
@app.errorhandler(404)
def page_not_found(e):
    response = make_response(render_template('404.html'),404)
    return response

@app.errorhandler(500)
def internal_error(e):
    response = make_response(render_template('500.html'),500)
    return response