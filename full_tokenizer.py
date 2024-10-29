import re

FUNCTIONS = [
    'sin', 'cos', 'tan', 'csc', 'sec', 'cot', 'arcsin', 'arccos', 'arctan',
    'arccsc', 'arcsec', 'arccot', 'sinh', 'cosh', 'tanh', 'csch', 'sech',
    'coth', 'arcsinh', 'arccosh', 'arctanh', 'arccsch', 'arcsech', 'arccoth',
    'ln', 'log', 'exp', 'sqrt'
]

class TokenTypes:
    NUMBER = 'NUMBER'
    IDENTIFIER = 'IDENTIFIER'
    CONSTANT = 'CONSTANT'
    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    EXPONENTIATION = '^'
    PARENTHESIS_LEFT = '('
    PARENTHESIS_RIGHT = ')'

TokenSpec = [ 
    (r'^(?:\d+(?:\.\d*)?|\.\d+)', TokenTypes.NUMBER),
    (r'^\+', TokenTypes.ADDITION), 
    (r'^\-', TokenTypes.SUBTRACTION),
    (r'^\*', TokenTypes.MULTIPLICATION), 
    (r'^\/', TokenTypes.DIVISION),
    (r'^\^', TokenTypes.EXPONENTIATION),
    (r'^\(', TokenTypes.PARENTHESIS_LEFT), 
    (r'^\)', TokenTypes.PARENTHESIS_RIGHT),
    (r'^e', TokenTypes.CONSTANT),
    (r'^pi', TokenTypes.CONSTANT),
    (r'^\s+', None),
    (r'^[a-zA-Z_]*', TokenTypes.IDENTIFIER),
]

class Tokenizer:
    def __init__(self, input):
        self.input = input
        self.cursor = 0

    def has_more_tokens(self):
        return self.cursor < len(self.input)

    def match(self, regex, input_slice):
        matched = re.match(regex, input_slice)
        if matched is None:
            return None
        full_match = matched.group(0)
        if full_match in FUNCTIONS:
            self.cursor += len(full_match)
            return full_match
        else: 
            if full_match == 'pi':
                self.cursor += 1
            else: full_match = input_slice[0]
            self.cursor += 1
            return full_match

    def get_next_token(self):
        if not self.has_more_tokens():
            return None

        input_slice = self.input[self.cursor:]

        # tries to find the correct regex match and returns the correct value with type
        for regex, token_type in TokenSpec:
            token_value = self.match(regex, input_slice)
            if token_value is None:
                continue
            if token_type is None:
                return self.get_next_token()
            if token_type == 'IDENTIFIER':
                if len(token_value) == 1:
                    token_type = 'VARIABLE'
                else:
                    token_type = 'FUNCTION'  
            return {'type': token_type, 'value': token_value}

        raise SyntaxError(f'Unexpected token: "{input_slice[0]}"')

operators = {
    'u-': {'prec': 4, 'assoc': 'right'},  
    '^': {'prec': 4, 'assoc': 'right'},
    '*': {'prec': 3, 'assoc': 'left'},
    '/': {'prec': 3, 'assoc': 'left'}, 
    '+': {'prec': 2, 'assoc': 'left'},
    '-': {'prec': 2, 'assoc': 'left'}
}

def assert_valid(predicate):
    if not predicate:
        raise ValueError('Assertion failed due to invalid token')

def generate_ast(input):
    op_symbols = list(operators.keys())
    stack = []
    output = []

    def peek():
        return stack[-1] if stack else None

    def add_to_output(token):
        output.append(token)
    
    def is_function(token):
        if isinstance(token, str):
            return token.lower() in FUNCTIONS 
        else: return False

    def handle_pop():
        op = stack.pop()

        if op == '(':
            return

        if op == 'u-':
            return {'type': 'UnaryExpression', 'operator': '-', 'argument': output.pop()}

        if is_function(op):
            argument = output.pop()
            return {'type': 'Function', 'name': op, 'argument': argument}

        right = output.pop()
        left = output.pop()

        if op in op_symbols:
            return {
                'type': 'BinaryExpression',
                'operator': op,
                'left': left,
                'right': right
            }

    def handle_token(token, prev_token):
        if isinstance(token, float):
            add_to_output({'type': 'Number', 'value': token})
        elif isinstance(token, str) and token.isidentifier():
            if is_function(token):
                stack.append(token)
            else:
                add_to_output({'type': 'Variable', 'name': token})
        elif token in op_symbols:
            o1 = token
            o2 = peek()

            while (o2 and o2 != '(' and
                   (operators[o2]['prec'] > operators[o1]['prec'] or
                    (operators[o2]['prec'] == operators[o1]['prec'] and operators[o1]['assoc'] == 'left'))):
                add_to_output(handle_pop())
                o2 = peek()

            stack.append(o1)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while peek() != '(':
                assert_valid(len(stack) != 0)
                add_to_output(handle_pop())
            assert_valid(peek() == '(')
            stack.pop()
            if peek() and is_function(peek()):
                add_to_output(handle_pop())
        else:
            raise ValueError(f'Invalid token: {token}')
    
    tokenizer = Tokenizer(input)
    token = None
    prev_token = None
    while True:
        token = tokenizer.get_next_token()
        if not token:
            break

        # Handle implicit multiplication
        if prev_token and (
            (prev_token['type'] == TokenTypes.NUMBER or prev_token['type'] == 'VARIABLE') and
            (token['type'] == 'VARIABLE' or token['type'] == 'FUNCTION' or token['type'] == TokenTypes.CONSTANT)
        ):
            handle_token('*', prev_token)

        if token['value'] == '-' and (prev_token is None or prev_token['value'] == '(' or prev_token['value'] in op_symbols):
            handle_token('u-', prev_token)
        elif token['type'] == TokenTypes.NUMBER:
            handle_token(float(token['value']), prev_token)
        else:
            handle_token(token['value'], prev_token)

        prev_token = token

    while len(stack) != 0:
        assert_valid(peek() != '(')
        add_to_output(handle_pop())

    if len(output) == 0:
        return None
    elif len(output) == 1:
        return output[-1]
    else:
        while len(output) > 1:
            left = output.pop(0)
            right = output.pop(0)
            combined = {'type': 'BinaryExpression', 'operator': '*', 'left': left, 'right': right}
            output.insert(0, combined)
        return output[-1]

# Test cases
#ast = generate_ast('sin(2x)')
#print(ast)
#ast = generate_ast('xln(x)')
#print(ast)
#ast = generate_ast('pixe')
#print(ast)
#ast = generate_ast('-e^xcos(x)')
#print(ast)
#ast = generate_ast('pi*x*e')
#print(ast)