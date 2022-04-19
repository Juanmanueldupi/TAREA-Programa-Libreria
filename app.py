import json 
from os import abort
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():  
    return render_template('contact.html')

@app.route("/error")
def error():
    return abort (404)

app.run("0.0.0.0", 5000, debug=True)
