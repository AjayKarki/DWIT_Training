'''
Create a class in representing a classroom. It should have have the following attributes
'no_students' (private), 'teacher' (public) and 'class' (public).
Also define a method to print the private attribute.
All the attributes should be set via the constructor.
'''


class Classroom:
    def __init__(self, no_students, teacher, classroom_class):
        self.__no_students = no_students
        self.teacher = teacher
        self.classroom_class = classroom_class

    def get_students_no(self):
        print("Number of Students", self.__no_students)


cr = Classroom(9, "Shreyansh", "Python")
cr.get_students_no()
