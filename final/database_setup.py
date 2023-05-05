import mysql.connector as sql

# === ABOUT ===
# Use this as a library with live-running python to set up the server, helps from accidental running.
# === END ===

def db_create():
    conn = sql.connect(host="10.10.5.151", user="flask", password="password")
    cur = conn.cursor()
    # ^^^ setup initial connection
    # vvv make and save new database for TTRPG game
    cmd = "CREATE DATABASE bloodrite"
    cur.execute(cmd)
    conn.close()
    print("DATABASE CREATED")


def table_create():
    server = sql.connect(host="10.10.5.151", user="flask", password="password", database="bloodrite")
    db = server.cursor()
    # ^^^ setup
    # vvv create table in database
    db.execute('CREATE TABLE characters (charid INT NOT NULL AUTO_INCREMENT, name TEXT, description TEXT, job TEXT, location TEXT, age TEXT, gender TEXT, voice TEXT, PRIMARY KEY (charid))')
    print("table created successfully")
    db.close()