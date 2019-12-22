"""
Create a class in python representing a cube, it should take the length of each side via a constructor.
The class should have two methods, one returns the volume and other the total surface area.
"""


class Cube:
    def __init__(self, length):
        self.length = length

    def get_volume(self):
        return self.length ** 3

    def get_area(self):
        return 6 * self.length ** 2


length = int(input("Enter Length of side of cube"))
c = Cube(length)
print("Volume", c.get_volume())
print("TSA", c.get_area())
