# As funções de detecção de operadores
def is_cop(token):
    return token in ['<', '>', '<=', '>=', '==', '!=']

def is_eop(token):
    return token in ['+', '-']

def is_top(token):
    return token in ['*', '/']

def is_ident(token):
    return isinstance(token, str) and not token in ['begin', 'if', 'while', 'read', 'write', 'program', ';', 'end', 'do', ':=', '(', ')'] + [c for c in token if not c.isalnum()]

# Função para processar sequências
def sequence(non_term, sep, tokens):
    x1, remaining_tokens = non_term(tokens)
    if remaining_tokens and sep(remaining_tokens[0]):
        x2, remaining_tokens = sequence(non_term, sep, remaining_tokens[1:])
        return (remaining_tokens[0], x1, x2), remaining_tokens
    else:
        return x1, remaining_tokens

# Funções para processar comparações, expressões e termos
def comp(tokens):
    return sequence(expr, is_cop, tokens)

def expr(tokens):
    return sequence(term, is_eop, tokens)

def term(tokens):
    return sequence(fact, is_top, tokens)

# Funções para processar fatores e identificadores
def fact(tokens):
    token = tokens[0]
    if isinstance(token, int) or is_ident(token):
        return token, tokens[1:]
    elif token == '(':
        e, remaining_tokens = expr(tokens[1:])
        if remaining_tokens[0] == ')':
            return e, remaining_tokens[1:]
        else:
            raise Exception('Expected )')
    else:
        raise Exception('Invalid token')

def id(tokens):
    if is_ident(tokens[0]):
        return tokens[0], tokens[1:]
    else:
        raise Exception('Expected identifier')

# Função para processar estatísticas
def stat(tokens):
    token = tokens[0]
    if token == 'begin':
        seq, remaining_tokens = sequence(stat, lambda t: t == ';', tokens[1:])
        if remaining_tokens[0] == 'end':
            return ('begin', seq), remaining_tokens[1:]
        else:
            raise Exception('Expected end')
    elif token == 'if':
        c, remaining_tokens = comp(tokens[1:])
        if remaining_tokens[0] == 'then':
            x1, remaining_tokens = stat(remaining_tokens[1:])
            if remaining_tokens[0] == 'else':
                x2, remaining_tokens = stat(remaining_tokens[1:])
                return ('if', c, x1, x2), remaining_tokens
            else:
                raise Exception('Expected else')
        else:
            raise Exception('Expected then')
    # E assim por diante para os outros casos...

# A função principal do parser
def prog(tokens):
    if tokens[0] == 'program':
        y, remaining_tokens = id(tokens[1:])
        if remaining_tokens[0] == ';':
            z, remaining_tokens = stat(remaining_tokens[1:])
            if remaining_tokens[0] == 'end':
                return ('prog', y, z), remaining_tokens[1:]
            else:
                raise Exception('Expected end')
        else:
            raise Exception('Expected ;')
    else:
        raise Exception('Expected program')

# Teste
tokens = ['program', 'foo', ';', 'while', 'a', '+', 3, '<', 'b', 'do', 'b', ':=', 'b', '+', 1, 'end']
parsed, remaining_tokens = prog(tokens)
print(parsed)