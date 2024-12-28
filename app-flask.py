from flask import Flask, url_for, render_template, request, Blueprint, redirect, session

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")