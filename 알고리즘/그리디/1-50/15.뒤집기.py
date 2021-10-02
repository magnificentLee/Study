# 0111010 0:3, 1:4 but 뒤집을 경우 0:3, 1:2 따라서 1이 더 많지만 1을 뒤집는게 이상적임
"""
n = input()
result = [n[0]]
for i in range(1, len(n)):
    if n[i] != result[-1]:
        result.append(n[i])
zero = result.count("0")
one = result.count("1")
print(min(zero, one))
"""
n = input()
result = [n[0]]
for i in range(1, len(n)):
    if n[i] != result[-1]:
        result.append(n[i])
zero = result.count("0")
one = result.count("1")
print(min(zero, one))