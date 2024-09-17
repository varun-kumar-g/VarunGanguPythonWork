# Description
# Using the function Map, count the number of words that start with ‘S’ in input_list.
#
#
#
# Sample Input:
#
# ['Santa Cruz','Santa fe','Mumbai','Delhi']


import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

count = list(filter(lambda x: str(x).startswith("S"), input_list))

print(len(count))
