# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
     return '''<html>
                <head>
                    <title>Continuous Delivery Pipeline</title>
                    <style>
                        body { font-family: Arial, sans-serif; }
                        .container { margin: 20px; }
                        h1 { color: #2e3b4e; }
                        .content { margin-top: 20px; }
                        .footer { margin-top: 30px; font-size: 12px; color: #888; }
                        .list { list-style-type: square; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Welcome to the Continuous Delivery Pipeline Project</h1>
                        <p><b>Hello,</b></p>
                        <p><b>Project: Setting up a Continuous Delivery Pipeline with Git, Jenkins, Docker, and AWS ECS!!!</b></p>
                        
                        <div class="content">
                            <p><b>Hello, new Jenkins file uploaded</b></p>
                            <p><b>Thank you</b></p>
                            <p><b>Rajeshwari TR</b></p>
                            <p><b>Bangalore</b>, <b>Karnataka</b></p>
                        </div>

                        <div class="content">
                            <h2>Project Overview</h2>
                            <p>This project involves setting up a Continuous Delivery pipeline using various modern technologies. Here's what we've done so far:</p>
                            <ul class="list">
                                <li>Configured Jenkins for automation</li>
                                <li>Dockerized applications for consistency</li>
                                <li>Deployed to AWS ECS for scalable infrastructure</li>
                                <li>Implemented automated testing and deployment strategies</li>
                            </ul>
                        </div>

                        <div class="content">
                            <h2>Technologies Used</h2>
                            <p>We leveraged the following technologies:</p>
                            <ol>
                                <li>Git for version control</li>
                                <li>Jenkins for Continuous Integration/Continuous Deployment</li>
                                <li>Docker for containerization</li>
                                <li>AWS ECS for container orchestration</li>
                            </ol>
                        </div>

                        <div class="content">
                            <h2>Images of the Pipeline</h2>
                            <p>Here’s an image illustrating our pipeline:</p>
                            <img src="https://via.placeholder.com/500x300?text=CD+Pipeline" alt="CD Pipeline" />
                        </div>

                        <div class="footer">
                            <p>For more information, check out <a href="https://www.example.com" target="_blank">this documentation link</a>.</p>
                            <p>&copy; 2025 Rajeshwari TR. All Rights Reserved.</p>
                        </div>
                    </div>
                </body>
              </html>'''



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

