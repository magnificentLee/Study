import sys

t = int(input())

for i in range(t):
    a, b = sys.stdin.readline().split()
    a = int(a)
    print(b[: a - 1] + b[a:])
"""
a, b = input().split()
a = int(a)
print(b[: a - 1] + b[a:])
테스트
"""