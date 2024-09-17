input_list = list(range(1, 100))
output_dict = {}

for val in input_list:
    if val % 3 == 0:
        output_dict[val] = val ** 3
print(output_dict)

# the above code is written using Comprehensions below
print({val: val ** 3 for val in input_list if val % 3 == 0})
