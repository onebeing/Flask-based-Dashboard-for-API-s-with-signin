from flask import Flask ,request ,render_template ,redirect ,session,url_for
from flask_session import Session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/",methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get("username",False) != 'admin' or request.form.get("password",False) != '12345':
            error = "Invalid Credentials!! Please Try Again"
        else:
            return render_template("emailsending.html")
    return render_template("index1.html",error=error)

