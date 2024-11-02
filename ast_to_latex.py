
from eq_parser import generate_ast, CONSTANTS, Tokenizer

RIGHT = r'\right'
LEFT = r'\left'
CDOT = r'\cdot'
SQUARE_ROOT = r'\sqrt'

def to_latex(ast, prev_op=False):
    eq = ''
    if ast is None: 
        return eq
    
    ast_type = ast['type']
    if ast_type == 'Variable':
        name = ast['name']
        if name in CONSTANTS:
            eq += f'\\{name}'
        else: eq += name
    elif ast_type == 'Number':
        eq += str(ast['value'])
    elif ast_type == 'Function':
        arg = to_latex(ast['argument'])
        if ast['name'] == 'sqrt':
            eq += f'{SQUARE_ROOT} {{{arg}}}'
        else: eq += f'\\{ast['name']} {LEFT}( {arg} {RIGHT})'
    elif ast_type == 'BinaryExpression':
        left = to_latex(ast['left'], True)
        right = to_latex(ast['right'], True)
        op = ast['operator']
        if prev_op:
            if op in '+-':
                eq += f'{LEFT}( {left} {op} {right} {RIGHT})'
            elif op == '*':
                eq += f'{left} {CDOT} {right}'
            elif op == '/':
                div = r'\frac'
                eq += f'{div}{{{left}}}{{{right}}}'
            elif op == '^':
                eq += f'{left}{op}{{{right}}}'
        else:
            if op in '+-':
                eq += f'{left} {op} {right}'
            elif op == '*':
                eq += f'{left} {CDOT} {right}'
            elif op == '/':
                div = r'\frac'
                eq += f'{div}{{{left}}}{{{right}}}'
            elif op == '^':
                eq += f'{left}{op}{{{right}}}'
    elif ast_type == 'UnaryExpression':
        arg = ast['argument']
        arg_latex = to_latex(ast['argument'])
        arg_type = arg['type']
        if arg_type == 'Function' or (arg_type == 'BinaryExpression' and arg['operator'] in '+-'):
            eq += f'- {LEFT}( {arg_latex} {RIGHT})'        
        else: eq += f'- {arg_latex}'
    
    return eq

def latex_equation(eq):
    ast = generate_ast(eq)
    return to_latex(ast)

# print(to_latex(generate_ast('pixe')))
# print(to_latex(generate_ast('pi*x*e')))
# print(to_latex(generate_ast('phi*x*e')))
# print(latex_equation('5e^(omega*pi)+y'))
# print(latex_equation('sin(200.5x)'))
# ln = 'x*((cos(x)sin(x))+1)'
# print(latex_equation(ln))