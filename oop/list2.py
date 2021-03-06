import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://plusbim:psqlSU@localhost:5432/plusbim"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    flights = Flight.query.filter_by(origin="Paris").first()


    print(f"{flights.origin} to {flights.destination}, {flights.duration} minutes.")


if __name__ == "__main__":
    with app.app_context():
        main()
