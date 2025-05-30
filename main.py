#!/usr/bin/env python3
import json
import sys
from parser import parser
from interpreter import execute

args = sys.argv

if len(args) > 2:
    raise ValueError("Too many CLI arguments. Usage: python script.py <query>")

if len(args) < 2:
    raise ValueError("Not enough CLI arguments. Usage: python script.py <query>")

query = args[1]
print("Request:", query)

res = parser.parse(query)

if res:
    print("Result:", res)

    fp = open("test-data.json", encoding="utf-8")
    data = json.load(fp)
    fp.close()
    results = execute(res, data)
    fp = open("save.json", 'w')
    json.dump(results, fp)
    print("Data saved")
    fp.close()
