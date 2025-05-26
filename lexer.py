import ply.lex as lex

# Reserved keywords dict
reserved = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE'
}

# Keywords list
tokens = (
    'COMMA', 'EQUALS',
    'STRING', 'IDENTIFIER',
) + tuple(reserved.values())

# Simple tokens format definition
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_EQUALS = r'='

# IDENTIFIER format definition = Basically a string without quotes which is not a given keyword
def t_IDENTIFIER(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reserved.get(t.value.upper(), 'IDENTIFIER') # So reserved keywords are not mistaken with identifiers
    return t

# STRING format definition = Something that starts and ends with a quote
def t_STRING(t):
    r"""\'[^\']*\'"""
    t.value = t.value.strip("'")
    return t

# We ignore tabulations and new lines
t_ignore = ' \t\n'

# Error if somthing is not included in any of the above formats
def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
