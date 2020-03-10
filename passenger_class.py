from people_class import *

class Passenger(People):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

