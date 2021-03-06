from main import db
#from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class registrationForm(FlaskForm):  
    username = StringField('Username', [validators.Length(min=4, max=25)])  
    email = StringField('Email Address', [validators.Length(min=6, max=35)])  
    password = PasswordField('New Password', [  
        validators.DataRequired(),  
        validators.EqualTo('confirm', message='Passwords must match')  
    ])  
    confirm = PasswordField('Repeat Password')  
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()]) 
    submit = SubmitField('Complete Registeration')

class RegistrationForm(db.Model):
    __tablename__ = 'registrationforms'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    accept_tos = db.Column(db.Boolean)

    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, username, email, password, accept_tos):
        self.username = username
        self.email = email
        self.password = password
        self.accept_tos = accept_tos





"""

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

"""class RegistrationForm(Form):
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

@app.route("/register", methods=["GET", "POST"])
def register():
    pageName = "/register"
    if request.method == "GET":
        return render_template("register.html", pageName=pageName, current_time=datetime.utcnow())
    else:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        accept_tos = request.form["accept_tos"]
        noteUser = RegistrationForm(username=username, email=email, password=password, accept_tos=accept_tos)
        db.session.add(noteUser)
        db.session.commit()




"""
