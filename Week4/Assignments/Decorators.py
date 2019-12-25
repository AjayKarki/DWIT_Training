"""
Write a python class for person and it should set the name and age via a constructor.
Write a class method that takes input the name and DOB and returns the corresponding person object.
Also write a static method that takes age as an argument and tells us if the person is eligible to vote.
"""


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def set_name(cls,name,dob):
