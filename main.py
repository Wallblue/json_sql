#!/usr/bin/env python3

import sys
from parser import parser

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