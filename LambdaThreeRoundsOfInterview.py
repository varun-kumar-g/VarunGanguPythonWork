import ast
import sys

input_str1 = sys.stdin.read()
input_list1 = ast.literal_eval(input_str1)
input_str2 = sys.stdin.read()
input_list2 = ast.literal_eval(input_str2)
input_str3 = sys.stdin.read()
input_list3 = ast.literal_eval(input_str3)

set1 = {item.lower() for item in input_list1}
set2 = {item.lower() for item in input_list2}
set3 = {item.lower() for item in input_list3}

union = set1.intersection(set2).intersection(set3)
print(sorted(union))
