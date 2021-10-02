"""
a = [103, 102, 171, 191]
b = [-13, 12, 11, 10]
result = []
for i in range(len(a)):  # 4 (0, 1, 2, 3)
    result.append(a[i] + b[i])
print(result)
"""
a = [103, 102, 171, 191]
b = [-13, 12, 11, 10]
print([a + b for a, b in zip(a, b)])