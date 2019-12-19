class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def print_sal(self):
        print(self.__salary)


e = Employee("RAM", 10000)
e.print_sal()
# print(e.__salary)
# del e
# print(e)