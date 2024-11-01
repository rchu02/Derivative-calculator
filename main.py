from latex2sympy2 import latex2latex
from ast_to_latex import latex_equation, RIGHT, LEFT
import sys

def display_diff(eq):
    diff = r"\frac{d}{dx}"
    return f'{diff}  {LEFT}({latex_equation(eq)}{RIGHT})'

def differentiation_solver(eq):
    return latex2latex(eq)

# x = 'e^(e^(e^(x)))'
# diff = display_diff(x)
# print(diff)
# print(differentiation_solver(diff))

if __name__ == "__main__":
    eq = input("Input your equation to differentiate: ")
    try:
        diff = display_diff(eq)
        print(f"\nThis is your equation in LaTeX: {display_diff(eq)}\n")
    except:
        print("Invalid Equation")
        sys.exit(0)
    
    proc = input("Y/N to differentiate: ")
    if proc == "Y" or proc == "y":
        print(f"\nYour Differentiated equation \n {differentiation_solver(diff)}")
    else:
        sys.exit(0)