"""
Create a new Database called ‘FinalYears’. Create a Table ‘Student’ with ‘USN’,’Name’ and ‘Age’ as fields.
Write a program to insert your USN, Name and Age information into the table.
"""
import pymysql

con = pymysql.connect(db="finalyears", user="root", password="", host="localhost")

cor = con.cursor()

try:
    sql = """
CREATE TABLE Student (usn int PRIMARY KEY auto_increment,name varchar (200),age int)"""
    cor.execute(sql)
except Exception as ex:
    # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    # message = template.format(type(ex).__name__, ex.args)
    # print(message)
    pass
flag = True
while flag:
    input_name = input('Enter Name')
    input_age = int(input('Enter Age'))
    cor.execute("INSERT INTO Student (name,age) VALUES (%s,%s)", (input_name, input_age))
    con.commit()
    flag = False if input("Want to enter more (y/n)") == 'n' else True

sql = "select * from Student"
cor.execute(sql)
result = cor.fetchall()
print(result)
