'''
Write a Python class named Circle constructed by a radius
and two methods which will compute the area and the perimeter of a circle
'''

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius


rad = float(input("Enter radius"))
c = Circle(rad)
print("Area is %.2f" % c.get_area())
print("Perimeter is %.2f" % c.get_perimeter())
