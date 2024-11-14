import sqlite3

connection = sqlite3.connect("temp_student.db")

cursor = connection.cursor()

##create table;

table_info ="""
            create table Student(Name varchar(25),
            class varchar(20),
            section varchar(20),
            marks int)
            """
            
cursor.execute(table_info)


cursor.execute('''INSERT INTO STUDENT VALUES ('TANISHQ' ,'AI', 'A' ,80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('STUD1' ,'CYBER', 'A' ,60)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('STUD2' ,'CS', 'B' ,70)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('STUD3' ,'ECE', 'A' ,67)''')

print("the selected records are")

data = cursor.execute(''' SELECT * FROM STUDENT''')

for row in  data:
    print(row)
    
    
connection.commit()
connection.close()