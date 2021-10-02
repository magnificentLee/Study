# 최소한을 물어보므로 그리디 알고리즘을 생각하자
"""
import sys

a, b = map(int, input().split())
coin = []
result = 0
for i in range(a):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)
for i in coin:
    if b == 0:
        break
    result += b // i
    b %= i
print(result)
"""
import sys

n, k = map(int, input().split())
coin = []
result = 0
for i in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)
for i in coin:
    if k == 0:
        break
    result += k // i
    k %= i
print(result)
