from sys import stdin

n, m = map(int, stdin.readline().split())
result = 0

for _ in range(n):
    data = map(int, stdin.readline().split())
    result = max(result, min(data))
print(result)