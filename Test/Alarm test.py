import sys

h, m = map(int, sys.stdin.readline().split())
if m < 45:
    if h == 0:
        print(h + 23, m + 15)
    else:
        print(h - 1, m + 15)
else:
    print(h, m - 45)