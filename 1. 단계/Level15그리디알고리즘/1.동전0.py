from sys import stdin
n, k = map(int, stdin.readline().rstrip().split())
coin = []
result = 0
for _ in range(n):
    coin.append(int(stdin.readline()))
coin.sort(reverse=True)
for i in coin:
    if k // i != 0:
        result += k // i
    k %= i
print(result)