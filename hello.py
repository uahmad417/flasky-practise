from datetime import datetime
from flask import (
    abort,
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
    session,
    flash
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# creating flask application instance
app = Flask(__name__)

# configuring application
app.config['SECRET_KEY'] = 'hard to guess string' 

# initializing flask extensions
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    response = make_response(render_template('404.html'),404)
    return response

@app.errorhandler(500)
def internal_error(e):
    response = make_response(render_template('500.html'),500)
    return response

# root URL
@app.route('/', methods=['GET', 'POST'])
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

@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session['name']
        new_name = form.name.data
        if new_name != old_name and old_name is not None:
            flash("Looks like you have changed your name")
        session['name'] = new_name
        return redirect(url_for('form_page'))
    response = make_response(render_template('form.html', form=form, name=session.get('name')))
    return response

# error handling views