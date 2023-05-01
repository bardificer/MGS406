import mysql.connector as sql
conn = sql.connect(host="10.10.5.151", user="flask", password="password")
cur = conn.cursor()
# Test connection (this step is optional)
print(conn)
cmd = "CREATE DATABASE flask_db"
cur.execute(cmd)
conn.close()