from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_image():
    return "<img src='/static/cours10.svg' width=\"5000px\"></img>"