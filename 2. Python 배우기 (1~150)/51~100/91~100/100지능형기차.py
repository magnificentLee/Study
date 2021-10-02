import sys

old_total = 0
max_total = 0
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    total = old_total + b - a
    if total > old_total:
        max_total = total
    old_total = total
print(max_total)