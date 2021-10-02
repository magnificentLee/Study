n = int(input())
a = n
for i in range(n):
    print(" " * i + "*" * (2 * (a - i) - 1))
