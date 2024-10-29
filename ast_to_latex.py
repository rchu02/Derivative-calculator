from full_tokenizer import generate_ast

#x_cosx = generate_ast('xcos(x)+sin(xyz)/y')
#x = generate_ast('x^3')
#ucosx = generate_ast('-(xcos(x)+sin(x))')
#sqrt = generate_ast('sqrt(x+2)')

RIGHT = r'\right'
LEFT = r'\left'
cdot = r'\cdot'
square_root = r'\sqrt'

def to_latex(ast):
    eq = ''
    if ast is None: 
        return eq
    
    ast_type = ast['type']
    if ast_type == 'Variable':
        eq += ast['name']
    elif ast_type == 'Number':
        eq += str(ast['value'])
    elif ast_type == 'Function':
        arg = to_latex(ast['argument'])
        if ast['name'] == 'sqrt':
            eq += f'{square_root} {{{arg}}}'
        else: eq += f'\\{ast['name']} {LEFT}( {arg} {RIGHT})'
    elif ast_type == 'BinaryExpression':
        left = to_latex(ast['left'])
        right = to_latex(ast['right'])
        op = ast['operator']
        if op in '+-':
            eq += f'{left} {op} {right}'
        elif op == '*':
            eq += f'{left} {cdot} {right}'
        elif op == '/':
            div = r'\frac'
            eq += f'{div}{{{left}}}{{{right}}}'
        elif op == '^':
            eq += f'{left}^{{{right}}}'
    elif ast_type == 'UnaryExpression':
        argu = to_latex(ast['argument'])
        eq += f'- {LEFT}( {argu} {RIGHT})'
    
    return eq

#print(to_latex(x_cosx))
#print(to_latex(x))
#print(to_latex(ucosx))
#print(to_latex(sqrt))