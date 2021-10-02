n = int(input())
a = n
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (a - i)) + "*" * i)
for j in range(1, n):
    print("*" * (a - j) + " " * (2 * j) + "*" * (a - j))
