from sys import stdin
n = int(stdin.readline())
time = [list(map(int, stdin.readline().split())) for _ in range(n)]
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
last = 0
result = 0
for i, j in time:
    if i >= last:
        result += 1
        last = j
print(result)