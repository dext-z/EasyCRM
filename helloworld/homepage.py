print('Hello Team, this is the EASY CRM')
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

print ('4')

#add description
print ('another')