from flask import Flask, url_for, render_template, request, Blueprint, redirect, session

app = Flask(__name__)

@app.route("\main")
def hello():
    print("hello world")
    return render_template("main.html")