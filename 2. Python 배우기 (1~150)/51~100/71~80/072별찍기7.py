n = int(input())
a = n

for i in range(1, a + 1):
    print(" " * (a - i) + "*" * (2 * i - 1))
for j in range(1, a):
    print(" " * j + "*" * (2 * (a - j) - 1))
