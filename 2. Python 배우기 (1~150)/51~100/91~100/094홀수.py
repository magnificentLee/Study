import sys

data = []

for i in range(7):
    n = int(sys.stdin.readline())
    if n % 2 == 1:
        data.append(n)
if not data:
    print(-1)
else:
    print(sum(data), min(data), sep="\n")