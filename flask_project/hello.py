from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my flask project. :)'

@app.route('/greetings/christmas')
def chrimus():
    return 'Merry Christmas!'

@app.route('/greetings/newyear')
def year():
    return 'Happy New Year!'


if __name__ == "__main__":
    app.run()
