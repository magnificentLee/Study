n, m = map(int, input().split())
array = [input() for _ in range(n)]
# 행 판별
result = 0
for i in range(n):
    idx = 0
    while idx < m:
        if array[i][idx] == "-":
            result += 1
            while idx < m and array[i][idx] == "-":
                idx += 1
        else:  # array[i][idx] == "|"
            idx += 1
# 열 판별
for j in range(m):
    idx = 0
    while idx < n:
        if array[idx][j] == "-":
            idx += 1
        else:
            result += 1
            while idx < n and array[idx][j] == "|":
                idx += 1
print(result)