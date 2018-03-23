import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://plusbim:psqlSU@localhost:5432/plusbim"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    r = csv.reader(f)

    for origin, destination, duration in r:
        print("data")
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight form {flight.origin} to {flight.destination} lasting {flight.duration} minutes.")

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
