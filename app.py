from flask import Flask, render_template, request, redirect, url_for
from diff_solver import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/", methods=['POST'])
def render():
    if request.form['button'] == "render":
        try:
            user_input = request.form.get("latexInput")
            equation = display_diff(user_input)
            return render_template("main.html", equation = equation, latex_equation = equation, user_input = user_input)
        except Exception as e:
            e = f'\\text{{{e}}}'
            return render_template("main.html", equation = e, user_input = user_input)
    elif request.form['button'] == "Derivitate!":
        equation = request.form.get("hiddenOutput")
        user_input = request.form.get("latexInput")
        derivative = differentiation_solver(equation)
        return render_template("main.html", equation = equation, latex_equation = equation, user_input = user_input, derivative = derivative)
    else:
        return {"error": "Something went wrong!"}, 404

if __name__ == "__main__":
    app.run(debug=True, port=8888)
    