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
    print(f"{flights.origin} to {flights.destination}, {flights.duration} minutes.")

    # order by usage
    flights = Flight.query.order_by(Flight.origin).all()
    print("Order by origin")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    # filter usage
    flights = Flight.query.filter(Flight.origin != "Paris").all()
    print("Filter by not equal to Paris")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #like usage
    flights = Flight.query.filter(Flight.origin.like("%a%")).all()
    print("Filter by contains %a%")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #in usage
    flights = Flight.query.filter(Flight.origin.in_(["Tokyo","Paris"])).all()
    print("Filter by in stament tokyo and paris")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #and usage
    flights = Flight.query.filter(Flight.origin == "New York",Flight.duration > 100).all()
    print("Filter by using and stament")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #or usage
    flights = Flight.query.filter(or_(Flight.origin == 'New York',Flight.duration > 100)).all()
    print("Filter by using or stament")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #join example
    flightpassengers = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    print("Flight - passenger list joined")
    for fp in flightpassengers:
        print(f"{fp.Flight.origin} to {fp.Flight.destination}, passenger name is {fp.Passenger.name}")

if __name__ == "__main__":
    with app.app_context():
        main()
