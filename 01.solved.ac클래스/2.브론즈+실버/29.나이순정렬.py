import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
    a, b = sys.stdin.readline().split()
    n.append((int(a), b, i))
n.sort(key=lambda x: (x[0], x[2]))
for i in range(t):
    print(n[i][0], n[i][1])