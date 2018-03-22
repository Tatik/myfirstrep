class Flight:

    counter = 1
    def  __init__(self, origin, destination, duration):
        #keep track of id number.
        self.id = Flight.counter
        Flight.counter +=1

        # keep track of passengers.
        self.passengers = []

        # details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def  print_info(self):
        print(f"Flight Origin: {self.origin}")
        print(f"Flight Destination: {self.destination}")
        print(f"Flight Duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")


    def delay(self, amount):
        self.duration += amount

    def  add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passanger:

    def __init__(self, name):
        self.name = name

def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    #create passengers.
    alice = Passanger(name="Alice")
    bob = Passanger(name="Bob")

    #add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()


if __name__ == "__main__":
    main()
