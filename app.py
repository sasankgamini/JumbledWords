from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import random
import os
app = Flask(__name__)

if os.environ.get("MONGO_URI") == None:
    file = open("connectionstring.txt","r")
    connectionstring = file.read().strip()
    file.close()
    app.config["MONGO_URI"] = connectionstring
    print('running on local server')
else:
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jumble", methods = ["GET", "POST"])
def jumble():
    if request.method == "GET":
        return render_template("jumble.html")
    else:
        word = request.form["wordEntered"]
        word = word.lower()
        wordlist = list(word)
        random.shuffle(wordlist)
        jumbledWord = "".join(wordlist)
        wordDB = {"originalWord":word, "jumbledWord":jumbledWord}
        mongo.db.words.insert_one(wordDB)
        return redirect("/jumble")

@app.route("/reveal")
def reveal():
    return "This is the reveal route"




if __name__ == "__main__":
    app.run(debug=True)