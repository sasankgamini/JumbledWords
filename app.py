from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jumble", methods = ["GET", "POST"])
def jumble():
    if request.method == "GET":
        return render_template("jumble.html")
    else:
        word = request.form["wordEntered"]
        print(word)
        return redirect("/jumble")

@app.route("/reveal")
def reveal():
    return "This is the reveal route"




if __name__ == "__main__":
    app.run(debug=True)