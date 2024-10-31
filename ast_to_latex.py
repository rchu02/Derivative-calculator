from full_tokenizer import generate_ast

#x_cosx = generate_ast('xcos(x)+sin(xyz)/y')
#x = generate_ast('x^3')
#ucosx = generate_ast('-(xcos(x)+sin(x))')
#sqrt = generate_ast('sqrt(x+2)')

RIGHT = r'\right'
LEFT = r'\left'
CDOT = r'\cdot'
SQUARE_ROOT = r'\sqrt'

def to_latex(ast):
    eq = ''
    if ast is None: 
        return eq
    
    ast_type = ast['type']
    if ast_type == 'Variable':
        if ast['name'] == 'phi':
            eq += r'\phi'
        elif ast['name'] == 'pi':
            eq += r'\pi'
        else: eq += ast['name']
    elif ast_type == 'Number':
        eq += str(ast['value'])
    elif ast_type == 'Function':
        arg = to_latex(ast['argument'])
        if ast['name'] == 'sqrt':
            eq += f'{SQUARE_ROOT} {{{arg}}}'
        else: eq += f'\\{ast['name']} {LEFT}( {arg} {RIGHT})'
    elif ast_type == 'BinaryExpression':
        left = to_latex(ast['left'])
        right = to_latex(ast['right'])
        op = ast['operator']
        if op in '+-':
            eq += f'{left} {op} {right}'
        elif op == '*':
            eq += f'{left} {CDOT} {right}'
        elif op == '/':
            div = r'\frac'
            eq += f'{div}{{{left}}}{{{right}}}'
        elif op == '^':
            eq += f'{left}^{{{right}}}'
    elif ast_type == 'UnaryExpression':
        argu = to_latex(ast['argument'])
        eq += f'- {LEFT}( {argu} {RIGHT})'
    
    return eq

def latex_equation(eq):
    ast = generate_ast(eq)
    return to_latex(ast)

#print(to_latex(x_cosx))
#print(to_latex(x))
#print(to_latex(ucosx))
#print(to_latex(sqrt))
#print(to_latex(generate_ast('pixe')))
#print(to_latex(generate_ast('pi*x*e')))
#print(to_latex(generate_ast('phi*x*e')))