from unicodedata import name
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/<name>")
def show_image(name=None):
    return render_template("index.html", name="/static/"+name)