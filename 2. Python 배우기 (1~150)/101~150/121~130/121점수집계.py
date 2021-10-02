import sys

t = int(input())

for i in range(t):
    n = sorted(map(int, sys.stdin.readline().split()))
    if n[3] - n[1] < 4:
        print(n[1] + n[2] + n[3])
    else:
        print("KIN")