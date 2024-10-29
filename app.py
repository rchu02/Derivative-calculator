from flask import Flask

app = Flask(__name__)

@app.route("\main.html")
def hello():
    return "Hello, World!"