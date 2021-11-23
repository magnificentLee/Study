# 1 2 3 4 5 6 7 8 9... (idx)
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5...
# 3 ~ 7 : 2 + 3 + 3 + 3 + 4
a, b = map(int, input().split())
result = []
tmp = 1
for _ in range(b):
    for _ in range(tmp):
        result.append(tmp)
    tmp += 1
print(sum(result[a - 1:b]))