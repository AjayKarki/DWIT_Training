class Person():
    def __init__(self, name):
        self.name = name

    def get_employee(self):
        print(self.name)


class Employee(Person):
    def __init__(self, name, types):
        # Person.__init__(self, name)
        super().__init__(name)
        self.types = types
        print("In class Employee")

    staff_number = 1007

    def get_employee(self):
        print(self.types)


class Animal:

    def needs_food(self):
        return True


class Engineer(Employee, Animal):
    def __init__(self, name1, types1, degree):
        super().__init__(name = name1, types=types1)  # this way we dont have to worry about order
        self.degree = degree

    def get_employee(self):
        """MRO - MEthod resolution order, when we call function from Engineer suru ma tyoo function aafnai class ma xa ki xaina herxa
        tes paxi employee ma khojxa ani tespaxi person ma khojxa...ani persion ma ni xaina  vane enginer ko aru kunai parent ma search garxa

        katai napaye object class ma khojxa...yo sab DFS-Depth First Search use garxa"""
        Person.get_employee(self)
        Employee.get_employee(self)
        print(self.degree)


y = Engineer("Ram", "Engineer", "BE")
y.get_employee()
print(y.needs_food())
print(Engineer.__mro__)