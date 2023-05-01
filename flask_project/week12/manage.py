import mysql.connector as sql
import mysql
from flask import Flask, render_template, request, send_file
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return send_file('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        try:
            msg='we failed'
            eid = request.form['eid']
            name = request.form['name']
            gender = request.form['gender']
            phone = request.form['phone']
            bday = request.form['bday']

            with sql.connect(host="10.10.5.151", user="flask", password="password", database="flask_db") as db:
                cur = db.cursor()
                print('1')
                cur.execute("INSERT INTO Employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(eid,name,gender,phone,bday))
                print('1')
                db.commit()
                print('1')
                msg="Record successfully added"
                print('1')

        except:
            db.rollback()
            msg="error in insert operation"

        return render_template("result.html",msg=msg)
        db.close()


@app.route('/information')
def info():
    db = sql.connect(host="10.10.5.151", user="flask", password="password", database="flask_db")
    cur = db.cursor(dictionary=True)
    cur.execute("select * from Employee")
    rows = cur.fetchall();
    print(rows)
    return render_template("info.html",rows = rows)