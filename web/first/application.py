from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Merhaba, web dünyası! desem"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Merhaba, {name}!</h1>"
