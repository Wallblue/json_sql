import ply.yacc as yacc
from lexer import tokens

# Query format definition
def p_query(p):
    """query : select_query"""
    p[0] = p[1]

# Select query formats definition
def p_select_query(p):
    """select_query : SELECT field_list FROM IDENTIFIER WHERE or_condition_list
                    | SELECT field_list FROM IDENTIFIER
                    | SELECT field_list WHERE or_condition_list
                    | SELECT field_list"""
    if len(p) == 7:
        # SELECT field FROM TABLE WHERE field = value
        p[0] = ('SELECT_FROM', p[2], p[4], p[6])
    elif len(p) == 5 and p[3] == 'FROM':
        # SELECT field FROM TABLE
        p[0] = ('SELECT_ALL_FROM', p[2], p[4])
    elif len(p) == 5 and p[3] == 'WHERE':
        # SELECT field WHERE field = value
        p[0] = ('SELECT', p[2], p[4])
    elif len(p) == 3:
        # SELECT field
        p[0] = ('SELECT_ALL', p[2])

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
def p_scalar_comparison_operand(p):
    """scalar_comparison_operand : EQUALS
                                 | LOWER
                                 | GREATER"""
    p[0] = p[1]

def p_array_comparison_operand(p):
    """array_comparison_operand : EQUALS
                                | IN"""
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

# List formats definitions
def p_field_list(p):
    """field_list : IDENTIFIER
                  | field_list COMMA IDENTIFIER"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

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

# Condition format definitions
def p_condition(p):
    """condition : scalar_condition
                 | array_condition"""
    p[0] = p[1]

def p_scalar_condition(p):
    """scalar_condition : IDENTIFIER scalar_comparison_operand scalar_value"""
    p[0] = (p[1], p[2], p[3], 'SCALAR')

def p_array_condition(p):
    """array_condition : IDENTIFIER array_comparison_operand array"""
    p[0] = (p[1], p[2], p[3], 'ARRAY')

# Error if the request doesn't fit the query format
def p_error(p):
    print("Erreur de syntaxe:", p)

parser = yacc.yacc()
