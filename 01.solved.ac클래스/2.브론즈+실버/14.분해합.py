import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    n_list = list(map(int, str(i)))
    result = i + sum(n_list)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
