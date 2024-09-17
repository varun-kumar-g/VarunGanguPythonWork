def sf(a):
    return a % 4 == 0 and a % 8 != 0
m = filter(sf, range(10, 31))
print(list(m))
