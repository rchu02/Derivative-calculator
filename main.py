from latex2sympy2 import latex2latex
from ast_to_latex import latex_equation, RIGHT, LEFT
import sys
import time

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
        start_time = time.time()
        diff = display_diff(eq)
        print(f"\nThis is your equation in LaTeX: {display_diff(eq)}\n")
        print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print("Invalid Equation")
        sys.exit(0)
    
    proc = input("Y/N to differentiate: ")
    start_time = time.time()
    if proc == "Y" or proc == "y":
        print(f"\nYour Differentiated equation \n {differentiation_solver(diff)}")
    else:
        sys.exit(0)
    start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))