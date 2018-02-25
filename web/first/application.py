from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Merhaba, web dünyası! desem"

@app.route("/tamer")
def tamer():
    return "Merhaba, Tamer"
