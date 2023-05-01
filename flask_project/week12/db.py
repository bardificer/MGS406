import mysql.connector as sql
server = sql.connect(host="10.10.5.151", user="flask", password="password", database="flask_db")
print("Opened database successfully")
db = server.cursor()
db.execute('CREATE TABLE Employee (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate TEXT)')
print("table created successfully")
db.close()