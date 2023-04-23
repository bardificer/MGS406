import sqlite3 as sql


db = sql.connect('database.db')
print("Opened database successfully")

db.execute('CREATE TABLE Employee (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate TEXT)')
print("table created successfully")
db.close()