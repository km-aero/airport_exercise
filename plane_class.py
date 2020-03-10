from aircraft_class import *

class Plane(Aircraft):
    def __init__(self, cargo, plane_number):
        super().__init__(cargo)
        self.plane_number = plane_number