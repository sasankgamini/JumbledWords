from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jumble")
def jumble():
    return render_template("jumble.html")

@app.route("/reveal")
def reveal():
    return "This is the reveal route"




if __name__ == "__main__":
    app.run(debug=True)