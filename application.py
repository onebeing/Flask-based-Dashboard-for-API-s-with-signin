import random
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("indexx.html")
@app.route("/next1")
def nextpage1():
    x = random.randint(0 ,100)
    return render_template("hello.html" ,number = x)

@app.route("/coinflip")
def toss():
    x = random.randint(0,1)
    return render_template("hello.html" ,toss = x)
@app.route("/user")
def userin():
    name = request.args.get("name")
    if not name:
        return render_template("fail.html")
    return render_template("userin.html" ,name=name)

