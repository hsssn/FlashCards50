import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///flashcards.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username")

        elif not request.form.get("password"):
            return apology("must provide password")

        elif not request.form.get("confirmation"):
            return apology("must confirm password")

        register_name = request.form.get("username")
        register_password = request.form.get("password")
        register_confirmation = request.form.get("confirmation")

        check_username = db.execute("SELECT * FROM user WHERE username = ?", register_name)
        if len(check_username) == 1:
            return apology("username unavailable")
        if len(register_password) < 8:
            return apology("password must be 8 characters or longer")
        if register_password != register_confirmation:
            return apology("confirmation does not match the password")

        db.execute("INSERT INTO user (username, hash) VALUES (?, ?) ", register_name, generate_password_hash(register_password))

        register_complete = db.execute("SELECT * FROM user WHERE username = ?", register_name)

        session["user_id"] = register_complete[0]["id"]

        create_q = 'CREATE TABLE IF NOT EXISTS ' + register_name + ' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, word TEXT NOT NULL, meaning TEXT NOT NULL)'

        db.execute(create_q)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        usernamee = request.form.get("username")

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM user WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]


        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        word = request.form.get("word")
        meaning = request.form.get("meaning")

        if word == None or meaning == None:
            return apology("must provide a word", 403)
        
        user_id = session["user_id"]
        username = db.execute("SELECT username FROM user WHERE id = ?", user_id)[0]["username"]
        db.execute("INSERT INTO ? (word, meaning) VALUES (?, ?) ", username, word, meaning)

        return redirect("/add")

    else:
        return render_template("add.html")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/practice")
@login_required
def practice():
    user_id = session["user_id"]
    username = db.execute("SELECT username FROM user WHERE id = ?", user_id)[0]["username"]
    termdata = db.execute("SELECT word, meaning FROM ?", username)

    return render_template("practice.html", termdata=termdata)


@app.route("/quiz")
@login_required
def quiz():
    user_id = session["user_id"]
    usernamee = db.execute("SELECT username FROM user WHERE id = ?", user_id)[0]["username"]
    termdata = db.execute("SELECT word, meaning FROM ?", usernamee)

    return render_template("quiz.html", termdata=termdata)

@app.route("/vocab", methods=["GET", "POST"])
@login_required
def vocab():

    user_id = session["user_id"]
    username = db.execute("SELECT username FROM user WHERE id = ?", user_id)[0]["username"]
    vocabs = db.execute("SELECT word, meaning, id FROM ?", username)

    if request.method =="POST":
        delete_word = request.form.get("valuee") 
        db.execute("DELETE FROM ? WHERE id = ?", username, delete_word)
        vocabs = db.execute("SELECT word, meaning, id FROM ?", username)
        return render_template("vocab.html", vocabs=vocabs)
    
    else:
        return render_template("vocab.html", vocabs=vocabs)
    
    
