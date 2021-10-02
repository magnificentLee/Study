"""
t = int(input())
n = [int(input()) for _ in range(t)]
result = 0
for i in range(t - 1, 0, -1):
    if n[i - 1] >= n[i]: # 이전 값이 다음 값보다 크거나 같은 경우 5 5 인 경우 4 5 가 되야함
        result += n[i - 1] - n[i] + 1  # 따라서 두 값을 빼준 다음 +1을 해야 함
        n[i - 1] = n[i - 1] - 1
"""
from sys import stdin

t = int(stdin.readline())
n = [int(stdin.readline()) for _ in range(t)]
result = 0
for i in range(t - 1, 0, -1):
    if n[i - 1] >= n[i]:
        result += n[i - 1] - n[i] + 1
        n[i - 1] = n[i] - 1
print(result)