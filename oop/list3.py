import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://plusbim:psqlSU@localhost:5432/plusbim"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    flightOrigin = "Tokyo"
    flights = Flight.query.filter_by(origin=flightOrigin).count()


    if flights > 1:
        print(f"There are {flights} {flightOrigin} flights.")
    else:
        print(f"There is {flights} {flightOrigin} flight.")

if __name__ == "__main__":
    with app.app_context():
        main()
