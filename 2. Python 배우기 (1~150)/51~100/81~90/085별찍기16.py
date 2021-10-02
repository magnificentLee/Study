n = int(input())
a = n
for i in range(n):
    print(" " * (a - i - 1) + "*" + " *" * i)
