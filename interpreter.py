def execute(req, data):
    results = None
    match req[0].split('_')[0]:
        case 'SELECT':
            results = select(req, data)
    return results

def select(req, data):
    request = get_select_req_elements(req)
    res = []

    if 'table' in request:
        if request['table'] not in data:
            raise ValueError(f"Table '{request['table']}' doesn't exist.")
        records = data[request['table']]
    else:
        records = data

    for record in records:
        if 'conditions' not in request or meet_conditions(record, request['conditions']):
            record_res = {field: record.get(field) for field in request['fields']}
            res.append(record_res)

    return res

def get_select_req_elements(req):
    res = dict()
    match req[0]:
        case 'SELECT_FROM':
            res = {'fields' : req[1], 'table' : req[2], 'conditions' : req[3]}
        case 'SELECT_ALL_FROM':
            res = {'fields' : req[1], 'table' : req[2]}
        case 'SELECT':
            res = {'fields' : req[1], 'conditions' : req[2]}
        case 'SELECT_ALL':
            res = {'fields' : req[1]}
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
