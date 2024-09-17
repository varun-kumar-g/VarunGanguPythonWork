import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
dictOutput = []
listLengths = []
for value in input_list:
    listLengths.append(len(value))

length_ordered_data = sorted(listLengths, reverse=True)
for val in length_ordered_data:
    for a in input_list:
        if len(a) == val:
            dictOutput.append(a)
print(dictOutput)
