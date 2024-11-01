from ast_to_latex import latex_equation

def test_ast_to_latex_basic_ops():
    assert latex_equation('x+y') == r'x + y'
    assert latex_equation('x-y') == r'x - y'
    assert latex_equation('x*y') == r'x \cdot y'
    assert latex_equation('x/y') == r'\frac{x}{y}'
    assert latex_equation('x^y') == r'x^{y}'
    assert latex_equation('-x') == r'- x'
    assert latex_equation('2') == r'2'
    assert latex_equation('100') == r'100'
    assert latex_equation('450.001') == r'450.001'
    assert latex_equation('x  +    y') == r'x + y'

def test_ast_to_latex_functions():
    assert latex_equation('cos(x)') == r'\cos \left( x \right)'
    assert latex_equation('ln(x*y+2)') == r'\ln \left( x \cdot y + 2 \right)'
    assert latex_equation('tan(x-2)') == r'\tan \left( x - 2 \right)'
    assert latex_equation('arccoth(x/2)') == r'\arccoth \left( \frac{x}{2} \right)'
    assert latex_equation('sqrt(x/2)') == r'\sqrt {\frac{x}{2}}'

def test_ast_to_latex_brackets():
    assert latex_equation('cos((x+2)/y)') == r'\cos \left( \frac{\left( x + 2 \right)}{y} \right)'
    assert latex_equation('(x+y)*(x-y)') == r'\left( x + y \right) \cdot \left( x - y \right)'
    assert latex_equation('e^(x+1)') == r'e^{\left( x + 1 \right)}'

def test_ast_to_latex_implicit_multiplication():
    assert latex_equation('xy') == r'x \cdot y'
    assert latex_equation('cos(x)y') == r'\cos \left( x \right) \cdot y'

def test_ast_to_latex_unary():
    assert latex_equation('-xy') == r'- x \cdot y'
    assert latex_equation('-(x+y)') == r'- \left( x + y \right)'

def test_ast_to_latex_constants():
    assert latex_equation('cos(x*omega)') == r'\cos \left( x \cdot \omega \right)'
    assert latex_equation('Phivarepsilon') == r'\Phi \cdot \varepsilon'
    assert latex_equation('Phi*varesilo') == r'\Phi \cdot v \cdot a \cdot r \cdot e \cdot s \cdot i \cdot l \cdot o'
    # test below can be fixed as \frac{\pi}{e} - \phi \cdot i + \theta instead
    assert latex_equation('pi/e-phi*i+theta') == r'\left( \frac{\pi}{e} - \phi \cdot i \right) + \theta'

def test_ast_to_latex_complicated():
    assert latex_equation('e^(e^(e^(x)))') == r'e^{e^{e^{x}}}'
    assert latex_equation('x*(cos(x)sin(x)+1)') == r'x \cdot \left( \cos \left( x \right) \cdot \sin \left( x \right) + 1 \right)'