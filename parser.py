import ply.yacc as yacc
from lexer import tokens

# Query format definition
def p_query(p):
    """query : SELECT field_list FROM IDENTIFIER WHERE or_condition_list"""
    p[0] = ('SELECT', p[2], p[4], p[6])

# Value format definition
def p_value(p):
    """value : scalar_value
             | array"""
    p[0] = p[1]

def p_scalar_value(p):
    """scalar_value : NUMBER
                    | STRING
                    | BOOLEAN"""
    p[0] = p[1]

# Comparison operands definition
def p_comparison_operand(p):
    """comparison_operand : EQUALS
                          | LOWER
                          | GREATER"""
    p[0] = p[1]

# Value list format definition : 1 identifier or several comma-separated
def p_value_list(p):
    """value_list : value
                  | value_list COMMA value"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Array format definition
def p_array(p):
    """array : LBRACKET value_list RBRACKET"""
    p[0] = p[2]

# Field list format definition : 1 identifier or several comma-separated
def p_field_list(p):
    """field_list : IDENTIFIER
                  | field_list COMMA IDENTIFIER"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
'''
def p_condition_list(p):
    """condition_list : condition
                      | condition_list AND condition
                      | condition_list OR condition"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
'''
def p_and_condition_list(p):
    """and_condition_list : condition
                          | and_condition_list AND condition"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_or_condition_list(p):
    """or_condition_list : and_condition_list
                         | or_condition_list OR and_condition_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Condition format identifier
def p_scalar_condition(p):
    """scalar_condition : IDENTIFIER comparison_operand scalar_value"""
    p[0] = (p[1], p[2], p[3])

def p_array_condition(p):
    """array_condition : IDENTIFIER EQUALS array
                       | IDENTIFIER IN array"""
    p[0] = (p[1], p[2], p[3])

def p_condition(p):
    """condition : scalar_condition
                 | array_condition"""
    p[0] = p[1]

# Error if the request doesn't fit the query format
def p_error(p):
    print("Erreur de syntaxe:", p)

parser = yacc.yacc()
