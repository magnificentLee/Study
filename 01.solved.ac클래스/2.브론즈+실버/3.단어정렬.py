import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
    a, b = sys.stdin.readline().split()
    n.append((int(a), b, i))
n.sort(key=lambda x: (x[0], x[2]))
for i in n:
    print(i[0], i[1])
