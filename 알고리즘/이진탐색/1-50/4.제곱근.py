# 백준 13706 제곱근
from sys import stdin
input = stdin.readline

n = int(input())
start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    target = mid ** 2
    if target < n:
        start = mid + 1
    else:
        end = mid - 1
print(start)