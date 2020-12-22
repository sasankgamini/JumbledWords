from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import random
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sasank_23:23_sasank@databases.ju9ys.mongodb.net/jumbledWords?retryWrites=true&w=majority" 
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