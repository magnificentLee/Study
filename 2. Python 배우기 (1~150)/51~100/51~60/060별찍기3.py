"""n = int(input())

for i in range(1, n + 1):
    print("*" * n)
    n -= 1
"""
n = int(input())
for i in range(n, 0, -1):
    print("*" * i)