from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
import os

from flask_bootstrap import Bootstrap

#from flask.ext.admin import Admin
from flask_admin import Admin
from flask_moment import Moment
from datetime import datetime
from flask_script import Manager
from flask_wtf import FlaskForm

from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is really hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)
admin = Admin(app)
manager = Manager(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

"""
python
from main import db
db.create_all()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])  
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
 
    def __init__(self, username, email, password, accept_tos):
        self.username = username
        self.email = email
        self.password = password
        self.accept_tos = accept_tos
"""

from models import *


@app.route("/")
def home():
    pageName = "home"
    return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())


@app.route("/notes/create", methods=["GET", "POST"])
def create_note():
    pageName = "/notes/create"
    if request.method == "GET":
        return render_template("create_note.html", pageName=pageName, current_time=datetime.utcnow())
    else:
        title = request.form["title"]
        body = request.form["body"]
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return redirect("/notes/create", form=form, current_time=datetime.utcnow())

@app.route("/notes", methods=["GET", "POST"])
def notes():
    pageName = "/notes"
    notes = Note.query.all()
    return render_template("notes.html", notes=notes, pageName=pageName, current_time=datetime.utcnow())

"""
@app.route("/register", methods=["GET", "POST"])
def register():
    pageName = "/register"
    notes = Note.query.all()
    form = RegistrationForm(request.form)
    if request.method == "GET":
        return render_template("register.html", notes=notes, pageName=pageName, current_time=datetime.utcnow())
    else:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        accept_tos = request.form["accept_tos"]
        noteUser = RegistrationForm(username=username, email=email, password=password, accept_tos=accept_tos)
        db.session.add(noteUser)
        db.session.commit()
        return redirect("register.html", pageName=pageName, form=form, current_time=datetime.utcnow())

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= "/register"
    form = RegistrationForm(request.form)
    form2 = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', pageName=pageName, form=form, form2=form2, current_time=datetime.utcnow())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    manager.run(me)
