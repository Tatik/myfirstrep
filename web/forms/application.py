from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"]) #sayfa form dan çağrılmazsa yani GET request olursa için kontrol
def hello():
    if request.method == "GET":
        return "Lütfen önce formu doldurun..."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)