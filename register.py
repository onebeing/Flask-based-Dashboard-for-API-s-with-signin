from flask import Flask,render_template
import sqlite3 
  
app = Flask(__name__)


@app.route("/")
def index():
    connection = sqlite3.connect("user.db") 
  
    connection.row_factory = sqlite3.Row
    crsr = connection.cursor() 
    crsr.execute("SELECT * FROM users")
    rows = crsr.fetchall()
    return render_template("index.html",rows=rows)

