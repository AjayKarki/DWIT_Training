class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_perimeter(self):
        print(2 * (self.length + self.breadth))

    def get_area(self):
        print(self.length * self.breadth)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def get_perimeter(self):
        super().get_perimeter()

    def get_area(self):
        super().get_area()


r = Rectangle(4, 5)
s = Square(4)
r.get_area()
r.get_perimeter()
s.get_area()
s.get_perimeter()
