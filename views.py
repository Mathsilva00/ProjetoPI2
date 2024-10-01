from main import app 
from flask import render_template

#rotas
@app.route("/")
def index1 ():
    return render_template("index1.html")

app.route("/")
def index3() :
    return render_template("index3.html")

app.route("/")
def index3() :
    return render_template("index3.html")