import ast, sys

n = int(input())
comprehensionsList = {v * v for v in range(1, n + 1)}
print(sorted(comprehensionsList))
