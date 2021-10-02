import sys

t = int(sys.stdin.readline())
num = []
for _ in range(t):
    num.append(list(map(int, sys.stdin.readline().split())))
num.sort(key=lambda x: (x[1], x[0]))
for i in range(t):
    print(num[i][0], num[i][1])