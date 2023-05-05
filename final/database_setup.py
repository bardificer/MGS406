import mysql.connector as sql
conn = sql.connect(host="10.10.5.151", user="flask", password="password")
cur = conn.cursor()
# ^^^ setup initial connection
# vvv make and save new database for TTRPG game
cmd = "CREATE DATABASE bloodrite"
cur.execute(cmd)
conn.close()