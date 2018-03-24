import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tamer:psqlSU@localhost:5432/tamer"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    #isome usage of orm s
    flights = Flight.query.filter_by(origin="Paris").first()
    print(f"Before update {flights.origin} to {flights.destination}, {flights.duration} minutes.")
    flights.duration = 280
    id = flights.id

    db.session.commit()

    flights = Flight.query.get(id)
    print(f"After update {flights.origin} to {flights.destination}, {flights.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
