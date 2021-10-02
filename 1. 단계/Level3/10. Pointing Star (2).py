"""a = int(input())

for i in range(1, a + 1):
    print(" " * (a - 1) + "*" * i)
    a = a - 1"""
n = int(input())

for i in range(1, n + 1):
    print(" " * n, "*" * i)
    n -= 1
# 2차
""" 3차
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
"""