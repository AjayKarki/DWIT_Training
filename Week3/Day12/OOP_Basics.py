class Student:
    age = 10
    name = "RAM"

    def print_name(self):
        print(self.name)


s = Student()
s.print_name()
print(s.name, s.age)
s.name = "Rahul"
s.print_name()


class Teacher:

    first_name = "Shreyansh"
    last_name = "Lodha"

    def get_name(self):
        print(self.first_name,self.last_name)


t = Teacher()
t.get_name()