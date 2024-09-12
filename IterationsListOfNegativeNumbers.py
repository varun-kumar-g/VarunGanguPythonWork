# print(list(range(0, -101, 2))) -- this option is wrong
print(list(range(-100, -1, 2)))
print(sorted(set(range(-2, -101, -2))))

l = []
for i in range(-100, 0):
    if(i % 2 == 0):
        l.append(i)
print(l)
