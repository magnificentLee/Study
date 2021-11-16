from sys import stdin
input = stdin.readline

l = int(input())
n = int(input())
cake = [0] * (l + 1)  # 0 포함
player = [0] * (n + 1)  # 0 포함
max_tmp = 0  # 예상 승자의 보유개수
idx_tmp = 0  # 예상 승자의 인덱스값(예상 승자 번호)
for i in range(1, n + 1):  # 인덱스상 +1 해야되기 때문
    p, k = map(int, input().split())
    # 예상 승자
    tmp_cnt = k - p + 1
    if tmp_cnt > max_tmp:
        max_tmp = tmp_cnt
        idx_tmp = i
    # 실제 승자
    for j in range(p, k + 1):
        if not cake[j]:
            cake[j] = 1
            player[i] += 1
print(idx_tmp)
print(player.index(max(player)))


"""
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