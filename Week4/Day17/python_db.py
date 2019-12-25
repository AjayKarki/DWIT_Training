import pymysql

con = pymysql.connect(db="basics_database", user="root", password="", host="localhost")

cor = con.cursor()

try:
    sql = """
CREATE TABLE teacher (id int PRIMARY KEY auto_increment,name varchar (200),subject varchar (20))"""
    cor.execute(sql)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    pass
# sql = "INSERT INTO teacher (name, subject) values ('Shreyansh','Python' )"
# cor.execute(sql)
#
# sql = "INSERT INTO teacher (name, subject) values ('Nipendra','Maths' )"
# cor.execute(sql)
#
# sql = "INSERT INTO teacher (name, subject) values ('Hari','COA' )"
# cor.execute(sql)
# con.commit()

# sql = "UPDATE teacher set subject= 'BigData' where id = 3"
# cor.execute(sql)
# con.commit()

# sql = "delete from teacher where id = 2"
# cor.execute(sql)
# con.commit()

# sql = "select * from teacher"
# cor.execute(sql)
# result = cor.fetchall()

# sql = "alter table teacher add  column (age int)"
# cor.execute(sql)

# sql = "alter table teacher drop column age"
# cor.execute(sql)

# try:
#     sql = "create table subject(id int primary key,name varchar(250))"
#     cor.execute(sql)
# except Exception:
#     pass
# sql = "insert into subject (name) values ('python')"
# cor.execute(sql)
# con.commit()

# cor.execute("alter table teacher add column subject_id int")
# cor.execute("alter table teacher add  foreign key (subject_id) references subject(id)")

cor.execute("insert into teacher (name,subject,subject_id) values ('RAM','python',1)")
con.commit()
