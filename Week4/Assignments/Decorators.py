"""
Write a python class for person and it should set the name and age via a constructor.
Write a class method that takes input the name and DOB and returns the corresponding person object.
Also write a static method that takes age as an argument and tells us if the person is eligible to vote.
"""
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_name(cls, name, dob):
        tod = date.today()
        age = tod.year - int(dob.split('/')[0])
        return cls(name, age)

    @staticmethod
    def can_vote(age):
        return True if age >= 18 else False


p = Person("Ajay", 24)
p2 = Person.set_name("Sagar", "1997/12/12")
print(p.name, p.age)
print(p2.name, p2.age)
print(p2.name,"Can Vote?",p2.can_vote(p2.age))
