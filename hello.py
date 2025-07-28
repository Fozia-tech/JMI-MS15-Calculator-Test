from flask import Flask, render_template

app = Flask(__name__)


name_person = "Fozia SOmethng"
age_person = 18

#this is the landing page
@app.route("/")
def hello_world():
    return render_template("index.html",person=name_person,age = age_person)