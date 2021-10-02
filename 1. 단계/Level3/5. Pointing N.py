""" 1차 시도
import sys

n = int(sys.stdin.readline())
m = 0
for i in range(n):
    m += 1
    print(m)
"""
"""import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    print(i)
    n += 1
# 2차 시도 = 6번 완료후 수정한 것
"""
n = int(input())

for i in range(1, n+1):
    print(i)