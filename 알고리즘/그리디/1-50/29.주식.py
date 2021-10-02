from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    stock = list(map(int, stdin.readline().split()))
    first = stock[-1]
    result = 0
    for i in range(n - 2, -1, -1):  # n - 1 = first 이기 때문
        if stock[i] > first:
            first = stock[i]
        else:
            result += first - stock[i]
    print(result)
