class Teacher:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(self.name, self.age)

    def __str__(self):
        return "Teacher's name is " + self.name

    def __del__(self):
        print(self, "Is Destroyed")


t = Teacher("Shreyansh", 27)
t.get_details()
