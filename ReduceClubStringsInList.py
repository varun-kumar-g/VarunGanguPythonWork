import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

from functools import reduce

output = reduce(lambda x, y: x + ' ' + y, input_list)

print(output)
# write your code here.

# print()
