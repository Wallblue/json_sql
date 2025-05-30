import ply.lex as lex

# Reserved keywords dict
reserved = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'true': 'BOOLEAN',
    'false': 'BOOLEAN',
    'IN': 'IN',
    'OR': 'OR',
    'AND': 'AND'
}

# Keywords list
tokens = (
    'EQUALS', 'LOWER', 'GREATER',
    'STRING', 'IDENTIFIER', 'NUMBER',
    'COMMA', 'RBRACKET', 'LBRACKET'
) + tuple(set(reserved.values()))

# Simple tokens format definition
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_EQUALS = r'='
t_LOWER = r'<'
t_GREATER = r'>'
t_IN = r'IN'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['

# IDENTIFIER format definition = Basically a string without quotes which is not a given keyword
def t_IDENTIFIER(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER') # So reserved keywords are not mistaken with identifiers
    if t.type == 'IDENTIFIER':
        t.type = reserved.get(t.value.upper(), 'IDENTIFIER') # We test for upper and lower case

    return t

# STRING format definition = Something that starts and ends with a quote
def t_STRING(t):
    r"""\'[^\']*\'"""
    t.value = t.value.strip("'")
    return t

def t_NUMBER(t):
    r"""(0|[1-9][0-9]*)(\.(0|[0-9]*[1-9]))?"""
    t.value = float(t.value)
    return t

# We ignore tabulations and new lines
t_ignore = ' \t\n'

# Error if somthing is not included in any of the above formats
def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
