from latex2sympy2 import latex2latex
from ast_to_latex import to_latex
from full_tokenizer import generate_ast

def differentiation_solver(eq):
    diff = r"\frac{d}{dx}"
    return latex2latex(f'{diff}  ({eq})')

x_cosx = generate_ast('xcos(x)+sin(xyz)/y')
x = generate_ast('x^3')
ucosx = generate_ast('-(xcos(x)+sin(x))')
sqrt = generate_ast('sqrt(x+2)')

x_cosx = to_latex(x_cosx)
x = to_latex(x)
ucosx = to_latex(ucosx)
sqrt = to_latex(sqrt)
print(ucosx)

print(differentiation_solver(x_cosx))
print(differentiation_solver(x))
print(differentiation_solver(ucosx))
print(differentiation_solver(sqrt))