class Flight:

    def  __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def  print_info(self):
        print(f"Flight Origin: {self.origin}")
        print(f"Flight Destination: {self.destination}")
        print(f"Flight Duration: {self.duration}")

def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Shangai", duration=185)
    f2.print_info()

if __name__ == "__main__":
    main()
