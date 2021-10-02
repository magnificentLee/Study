# 1  4344ms 167B
"""
t = int(input())
n = []
for i in range(t):
    a, b = input().split()
    n.append((int(a), b, i))
n.sort(key=lambda x: (x[0], x[2]))
for i in n:
    print(i[0], i[1])
"""
# 2
"""
t = int(input())
n = []
for i in range(t):
    a, b = input().split()
    n.append((int(a), b, i))
n.sort(key=lambda x: (x[0], x[2]))
for i in range(t):
    print(n[i][0], n[i][1])
"""
# t 의 값이 10만 까지 가는것에 주목
# 3  364ms 205B
import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
    a, b = sys.stdin.readline().split()
    n.append((int(a), b, i))
n.sort(key=lambda x: (x[0], x[2]))
for i in n:
    print(i[0], i[1])