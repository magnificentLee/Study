import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
    n.append(int(sys.stdin.readline()))
n.sort()
print(*n, sep="\n")