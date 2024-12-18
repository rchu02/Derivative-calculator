from latex2sympy2 import latex2latex
from ast_to_latex import to_latex, latex_equation, RIGHT, LEFT
from eq_parser import generate_ast

def display_diff(eq):
    diff = r"\frac{d}{dx}"
    return f'{diff}  {LEFT}({latex_equation(eq)}{RIGHT})'

def differentiation_solver(eq):
    return latex2latex(eq)

x = 'e^(e^(e^(x)))'
diff = display_diff(x)
print(diff)
print(differentiation_solver(diff))

#x_cosx = generate_ast('xcos(x)+sin(xyz)/y')
#x = generate_ast('x^3')
#ucosx = generate_ast('-(xcos(x)+sin(x))')
#sqrt = generate_ast('sqrt(x+2)')

#x_cosx = to_latex(x_cosx)
#x = to_latex(x)
#ucosx = to_latex(ucosx)
#sqrt = to_latex(sqrt)

#print(differentiation_solver(x_cosx))
#print(differentiation_solver(x))
#print(differentiation_solver(ucosx))
#print(differentiation_solver(sqrt))