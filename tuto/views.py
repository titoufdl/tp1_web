from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "base.html",
        title="Hello World!")
    
@app.route("/noms")
def noms():
    return render_template(
        "noms.html",
        title="Hello World!",
        names=["Pierre", "Paul", "Corinne"])
    
        
