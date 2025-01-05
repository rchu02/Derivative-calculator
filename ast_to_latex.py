from eq_parser import generate_ast, CONSTANTS

RIGHT = r'\right'
LEFT = r'\left'
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
        op = ast['operator']
        if prev_op:
            if op in '+-':
                left = to_latex(ast['left'])
                right = to_latex(ast['right'])
                eq += f'{LEFT}( {left} {op} {right} {RIGHT})'
            elif op == '*':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
                eq += f'{left} {right}'
            elif op == '/':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
                div = r'\frac'
                eq += f'{div}{{{left}}}{{{right}}}'
            elif op == '^':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
                eq += f'{left}{op}{{{right}}}'
        else:
            if op in '+-':
                left = to_latex(ast['left'])
                right = to_latex(ast['right'])
                eq += f'{left} {op} {right}'
            elif op == '*':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
                eq += f'{left} {right}'
            elif op == '/':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
                div = r'\frac'
                eq += f'{div}{{{left}}}{{{right}}}'
            elif op == '^':
                left = to_latex(ast['left'], True)
                right = to_latex(ast['right'], True)
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