from sys import stdin
input = stdin.readline

cake = [1] * (int(input()) + 1)
n = int(input())
max_count = 0
max_n = 0
count_cake = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, input().split())
    count = b - a + 1
    if count > max_count:
        max_count = count
        max_n = i
    for j in range(a, b + 1):
        if cake[j] == 1:
            cake[j] = 0
            count_cake[i] += 1
print(max_n)
print(count_cake.index(max(count_cake)))