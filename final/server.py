import mysql.connector as sql
import mysql
from flask import Flask, render_template, request, send_file, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('character_submission.html')

@app.route('/submission', methods = ['POST','GET'])
def submission():
    if request.method == 'POST':
        try:
            msg='There was an error processing this request. Please contact the administrator.'
            name = request.form['name']
            desc = request.form['desc']
            job = request.form['job']
            loc = request.form['loc']
            age = request.form['age']
            gender = request.form['gender']
            voice = request.form['voice']

            with sql.connect(host="10.10.5.151", user="flask", password="password", database="bloodrite") as db:
                cur = db.cursor()
                cur.execute("INSERT INTO characters (name, description, job, location, age, gender, voice) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(name, desc, job, loc, age, gender, voice))
                db.commit()
                msg="Record successfully added"

        except:
            db.rollback()
            msg="ERROR IN INSERT OPERATION"

        return render_template("result.html",msg=msg)
        db.close()


@app.route('/char')
def info():
    try:
        char_id = int(request.args.get('id', ''))
    except:
        char_id = None

    if char_id == None:
        db = sql.connect(host="10.10.5.151", user="flask", password="password", database="bloodrite")
        cur = db.cursor(dictionary=True)
        cur.execute("select charid,name,location from characters")
        rows = cur.fetchall();
        print(rows)
        return render_template("list.html",rows = rows)

    db = sql.connect(host="10.10.5.151", user="flask", password="password", database="bloodrite")
    cur = db.cursor(dictionary=True)
    cur.execute("select * from characters where charid like '{0}'".format(char_id))
    result = cur.fetchone();
    print(result)
    return render_template("individual.html",result = result)
