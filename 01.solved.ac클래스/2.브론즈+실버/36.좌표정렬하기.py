import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t):
    result.append(list(map(int, sys.stdin.readline().split())))
result.sort(key=lambda x: (x[0], x[1]))
for i in result:
    print(i[0], i[1])