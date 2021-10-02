import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    count = 0
    for j in range(a, b + 1):
        c = str(j)
        count += c.count("0")
    print(count)