'''
Create a class in python called ‘student’, it should set name and roll via constructor.
Then make a class called ‘test’ which inherits student and sets the date of test via constructor.
Then create a class marks that sets marks of maths, science and English via constructor
and inherits the 'test' class.
Use an object of marks to access the name of corresponding student
'''


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Test(Student):
    def __init__(self, date_of_test, name, roll):
        super().__init__(name, roll)
        self.date_of_test = date_of_test


class Marks(Test):
    def __init__(self, maths, science, english, date_of_test, name, roll):
        super().__init__(date_of_test, name, roll)
        self.maths = maths
        self.science = science
        self.english = english


std_marks = Marks(89, 79, 88, "17th Nov", "Ram", 6)
print(std_marks.name)
