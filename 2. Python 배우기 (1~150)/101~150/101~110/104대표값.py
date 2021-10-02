import sys

data = []
for i in range(10):
    n = int(sys.stdin.readline())
    data.append(n)
print(sum(data) // 10)
print(max(data, key=data.count))
