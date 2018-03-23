import csv
import os

def main():

    f = open("flights.csv")
    r = csv.reader(f)

    for origin, destination, duration in r:
        print("data")
        print(f"Added flight form {origin} to {destination} lasting {duration} minutes.")

if __name__ == "__main__":
    main()
