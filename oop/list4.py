import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://plusbim:psqlSU@localhost:5432/plusbim"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    #instead od using this code flights = Flight.query.filter_by(id=1).first() that gets the record that its id=1
    #we can use below
    flights = Flight.query.get(1)
    print(f"The #1 flight is {flights.origin} to {flights.destination}.")

if __name__ == "__main__":
    with app.app_context():
        main()
