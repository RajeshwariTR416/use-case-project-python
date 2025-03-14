# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<b>Hello,</b><br><b>Project 6: Setting up a Continuous Delivery Pipeline with Git, Jenkins, Docker, and AWS ECS!!!
hello new jenkins file uploaded
Thank you</b>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

