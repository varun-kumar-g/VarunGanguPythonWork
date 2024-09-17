import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

output = [u for u in [str(u)[str(u).find('s'):str(u).find('p') + 1].strip() for u in input_list] if u != '']

# str(u)[str(u).find('s'):  str(u).find('p')

print(output)
