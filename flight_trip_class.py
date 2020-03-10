class FlightTrip:
    def __init__(self, origin='', destination='', list_of_passenger=[], plane_number='', flight_id):
        self.origin = origin
        self.destination = destination
        self.list_of_passenger = list_of_passenger
        self.plane_number = plane_number
        self.flight_id = flight_id

# use getters and setters

# As a user I can create a flight with no specific information
# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin
# As a user I can add a Passenger to the list of passengers
# Passenger list is a list of object that are Passenger