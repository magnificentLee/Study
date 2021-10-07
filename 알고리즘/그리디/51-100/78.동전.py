# 전에 작성했던 방식추가
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0
for i in coins:
    result += k // i
    k %= i
print(result)
"""
n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0
for i in range(n):
    result += k // coins[i]
    k -= (coins[i] * (k//coins[i]))
print(result)
"""
