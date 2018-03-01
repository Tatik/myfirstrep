import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://plusbim:psqlSU@localhost:5432/plusbim') #os.getenv("DATABASE_URL")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")

def index():
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book"):
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))

def main():
    # List all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin}: to {flight.destination}, {flight.duration} minutes.")

    # Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id": flight_id}).fetchone()

    # Make Sure flight tis valid.
    if flight is None:
        print("Error: No such flight.")
        return

    # List passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :id",{"id": flight_id}).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")

if __name__ == "__main__":
    main()
