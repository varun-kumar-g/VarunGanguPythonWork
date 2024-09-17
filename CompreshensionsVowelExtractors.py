import ast
import sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
outputList = list({a: None for a in input_list if str(a)[0] in "aeiou"}.keys())
print(outputList)
