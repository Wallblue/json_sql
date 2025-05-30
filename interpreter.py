def execute(req, data):
    results = None
    match req[0]:
        case 'SELECT':
            results = select(req, data)
    return results

def select(req, data):
    fields, table, conditions = req[1], req[2], req[3]
    res = []
    for record in data:
        if meet_conditions(record, conditions):
            record_res = {field: record.get(field) for field in fields}
            res.append(record_res)

    return res

def meet_conditions(record, conditions):
    return check_or_conditions(record, conditions)

def check_or_conditions(record, or_conditions):
    for or_cond in or_conditions:
        if isinstance(or_cond, list):
            if check_and_conditions(record, or_cond):
                return True
        elif check_condition(record, or_cond):
            return True
    return False

def check_and_conditions(record, and_conditions):
    for and_cond in and_conditions:
        if isinstance(and_cond, list):
            if not check_or_conditions(record, and_cond):
                return False
        elif not check_condition(record, and_cond):
            return False
    return True

def check_condition(record, condition):
    identifier, op, value, cond_type = condition
    true_value = record.get(identifier, None)
    match op:
        case '=':
            return value == true_value
        case '>':
            return value > true_value
        case '<':
            return value < true_value
        case '=':
            return value == true_value
        case 'IN':
            return true_value in value
    return False
