import sys

t = int(sys.stdin.readline())
result = []
for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0 and len(result) > 0:
        result.pop()
    else:
        result.append(n)
print(sum(result))