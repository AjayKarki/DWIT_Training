class Student:
    def __init__(self, name="", marks=""):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks

    @property
    def got_marks(self):
        return self.name + ' obtained ' + self.marks

    @got_marks.setter
    def got_marks(self, text):
        name, _, marks = text.split(' ')
        self.name = name
        self.marks = marks


st = Student("RAM", "25")
print(st.name, st.marks, st.got_marks)
st.name = "Hari"
print(st.got_marks)

st2 = Student()
st2.got_marks = "Sita got 100"
print(st2.name, st2.marks, st2.got_marks)
