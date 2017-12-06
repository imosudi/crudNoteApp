from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

from flask import Flask
from flask_bootstrap import Bootstrap

#from flask.ext.admin import Admin
from flask_admin import Admin


app = Flask(__name__)

bootstrap = Bootstrap(app)
#moment = Moment(app)
admin = Admin(app)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

"""
python
from main import db
db.create_all()
"""

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route("/")
def home():
    pageName = "home"
    return render_template("home.html", pageName=pageName)

@app.route("/notes/create", methods=["GET", "POST"])
def create_note():
    pageName = "/notes/create"
    if request.method == "GET":
        return render_template("create_note.html", pageName=pageName)
    else:
        title = request.form["title"]
        body = request.form["body"]
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return redirect("/notes/create")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    pageName = "/notes"
    notes = Note.query.all()
    return render_template("notes.html", notes=notes, pageName=pageName)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


