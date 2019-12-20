class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_perimeter(self):
        print(2 * (self.length + self.breadth))

    def get_area(self):
        print(self.length * self.breadth)


class EqualSidedShape:
    def isSymmetricalOnDiagonal(self):
        return True


class Square(Rectangle, EqualSidedShape):
    def __init__(self, length):
        Rectangle.__init__(self, length, length)

    def get_perimeter(self):
        super().get_perimeter()

    def get_area(self):
        super().get_area()


s = Square(4)
print(s.isSymmetricalOnDiagonal())
