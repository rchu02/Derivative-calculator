from latex2sympy2 import latex2latex

def differentiation_solver(eq):
    diff = r"\frac{d}{dx}"
    return latex2latex(f'{diff}  {eq}')

print(differentiation_solver('x\cdot2'))