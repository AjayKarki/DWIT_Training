"""
Polymorphism can be done in two ways function overloading and use of decorators

"""


# Method 1
# class Operation:
#     def sums(self, n1, b, c=0):
#         return n1 + b + c
#
#
# o = Operation()
# print(o.sums(1, 2, 3))
# print(o.sums(1, 2))


def sample_decorator(sample_function):
    def inner_function():
        from datetime import datetime
        file = open("text.txt", 'a')
        file.write('called' + str(datetime.now()) + '\n')
        file.close()
        print("I am decorator")
        return sample_function()

    return inner_function


@sample_decorator  # Now this is how you call a decorator
def test_function():
    print("I am a normal function")


# test_function = sample_decorator(test_function)  # write this if you aren't writing @sample_decorator
test_function()
# import time
# time.sleep(5)
test_function()
# time.sleep(5)
test_function()


class Employee:
    sal_raise = 0.05

    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal

    """changes class property rather than object property"""

    @classmethod
    def change_raise(cls, raise_per):
        """
        Manager aayo manager lai aba bata salary raise change garna mann lagyo re
        """
        cls.sal_raise = raise_per

    @classmethod
    def from_text(cls, text):
        name, age, salary = text.split(",")
        return cls(name, age, salary)

    @staticmethod  # can't use class attributes
    def print_hello():
        print("Hello!!!")


e = Employee("Gita", 18, 2000)
# print(e.sal_raise)
# Employee.change_raise(0.2)
# e2 = Employee()
# print(e2.sal_raise)

file = open('employee.csv', 'r')
for line in file.readlines():
    e = Employee.from_text(line)
Employee.print_hello()
