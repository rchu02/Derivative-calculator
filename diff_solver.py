from latex2sympy2 import latex2latex
from ast_to_latex import latex_equation, RIGHT, LEFT

def display_diff(eq):
    diff = r"\frac{d}{dx}"
    return f'{diff}  {LEFT}({latex_equation(eq)}{RIGHT})'

def differentiation_solver(eq):
    return latex2latex(eq)