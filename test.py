from latex2sympy2 import latex2sympy, latex2latex

tex = r"\frac{d}{dx}(-(x\cos(x)+\sin(x)))"

print(latex2sympy(tex))

print(latex2latex(tex))