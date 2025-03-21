# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''<b>Hello,</b><br>
<b>Project: Setting up a Continuous Delivery Pipeline with Git, Jenkins, Docker, and AWS ECS!!!</b><br>
<b>Hello, new Jenkins file uploaded</b><br>
<b>Thank you</b><br>
<b>Rajeshwari TR</b><br>
<b>Bangalore North</b>'''



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

