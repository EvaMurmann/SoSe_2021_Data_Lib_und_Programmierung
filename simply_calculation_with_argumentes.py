# -*- coding: utf-8 -*-

# Hello
"""
Hello script
"""

import argparse

parser = argparse.ArgumentParser()

# interface / API
parser.add_argument("number_1", type=int, help="An integer")
parser.add_argument("number_2", type=int, help="Another integer")
#parser.add_argument("-multi", default=False, action="store_true")

parser.add_argument("--operation", choices= ["div", "sub", "sum", "mult"])

# vergleich string 
if args.opertation == "div":
   result = args.number_1 / args.number_2
elif args.operation == "sub":
   result = args.number_1 - args.number_2
elif args.operation == "sum":
   result = args.number_1 + args.number_2
elif args.operation == "mult":
   result = args.number_1 * args.number_2

print(result)

#args = parser.parse_args()

#print(args)
#print(args.number_1, args.number_2)

#if args.multi:
#   result = args.number_1 * args.number_2
#else:
#    result = args.number_1 + args.number_2

#print(result)
