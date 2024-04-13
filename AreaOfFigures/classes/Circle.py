
from math import pi
class Circle():
    radius=0
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(pi*self.radius**2)
