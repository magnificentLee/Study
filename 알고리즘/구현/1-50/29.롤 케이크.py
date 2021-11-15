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
"""
l = int(input())
n = int(input())

cake = [0] * (l + 1)
players = [0] * (n + 1)

length_max = 0
idx = 0

for i in range(n):
    p, k = map(int, input().split())
    # 예상 승자
    if length_max < k - p:
        length_max = k - p
        idx = i + 1
    # 실제 승자
    result = 0
    for j in range(p, k + 1):
        if not cake[j]:
            cake[j] = 1
            result += 1
    players[i] = result
print(idx)
print(players.index(max(players)))
"""