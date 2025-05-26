import ply.yacc as yacc
from lexer import tokens

# Query format definition
def p_query(p):
    """query : SELECT field_list FROM IDENTIFIER WHERE condition"""
    p[0] = ('SELECT', p[2], p[4], p[6])

# Field list format definition : 1 identifier or several comma-separated
def p_field_list(p):
    """field_list : IDENTIFIER
                  | field_list COMMA IDENTIFIER"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Condition format identifier
def p_condition(p):
    """condition : IDENTIFIER EQUALS STRING"""
    p[0] = (p[1], '=', p[3])

# Error if the request doesn't fit the query format
def p_error(p):
    print("Erreur de syntaxe:", p)

parser = yacc.yacc()
