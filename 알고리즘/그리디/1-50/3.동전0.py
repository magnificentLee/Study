from sys import stdin
n, k = map(int, stdin.readline().split())
coin = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)
result = 0
for i in coin:
    result += k // i
    k %= i
print(result)