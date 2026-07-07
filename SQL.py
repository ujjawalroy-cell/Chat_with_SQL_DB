import sqlite3
connection = sqlite3.connect("Classroom.db")

cursor = connection.cursor()

table_info = """
create table Classroom(Name VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARK INT)
"""
cursor.execute(table_info)

cursor.execute('''insert into Classroom values('ujjawal','Data science','A',90)''')
cursor.execute('''insert into Classroom values('ishaan','Data science','B',100)''')
cursor.execute('''insert into Classroom values('saksham','Data science','C',80)''')
cursor.execute('''insert into Classroom values('saiyam','BBA','F',0)''')
cursor.execute('''insert into Classroom values('rajat','BMS','D',9)''')

cursor.execute('''SELECT * FROM Classroom ''')
connection.commit()
connection.close()