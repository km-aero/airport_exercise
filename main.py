from plane_class import *
from passenger_class import *
from people_class import *
from flight_trip_class import *

# Initialise lists
plane_list = []
passenger_list = []
flight_list = []

# I can create 'Joana Thomson' with the Passport number 'B343123'
# I can create 'Birt Kuman' with the Passport number 'B13927'

# Create planes
while True:
    plane_number = input('Please enter the plane_number or write \'exit\' to exit.\n')
    if 'exit' in plane_number:
        break
    else:
        cargo = input('Please enter the cargo size.\n')
        plane = Plane(plane_number, cargo)
        plane_list.append(plane)

[print(i.plane_number, i.cargo) for i in plane_list]

# Create Passengers
while True:
    name = input('Please enter the plane_number or write \'exit\' to exit.\n')
    if 'exit' in plane_number:
        break
    else:
        passenger_number = input('Please enter the cargo size.\n')
        passenger = Passenger(name, passenger_number)
        passenger_list.append(passenger)

[print(i.name, i.passenger_number) for i in passenger_list]

# Create flight trip
while True:
    question = input('Would you like to create a flight trip? y/n')
    if question == 'y':
        question = input('Would you like to add details? y/n')
        if question == 'y':
            origin = input('Please enter the origin of the flight.')
            destination = input('Please enter the destination of the flight.')
            list_of_passengers = input('Please enter the list of passengers.')
            plane_number = input('Please input the plane number of the flight.')
            flight_id = len(flight_list)
            flight_trip = FlightTrip(origin,destination,list_of_passengers,plane_number,flight_id)
        elif question == 'n':
            flight_trip = FlightTrip()
    elif question == 'n':
        print('Thanks')
        break