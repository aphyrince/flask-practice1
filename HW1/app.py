from flask import Flask, render_template

app = Flask(__name__)


my_hobby = ["youtube", "game", "diy"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html", hobbyList=my_hobby)


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)
