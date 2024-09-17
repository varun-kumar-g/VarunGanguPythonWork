import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

c = {v["rank"] for v in input_list}
e = {v["name"] for v in input_list}

dict = []

for b in c:
    for v in sorted(e):
        for c in input_list:
            if (c["name"] == v and c["rank"] == b):
                dict.append(c)
                break
print(dict)
