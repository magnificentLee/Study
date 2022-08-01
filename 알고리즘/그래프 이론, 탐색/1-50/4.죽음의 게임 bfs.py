# bfs로 풀것
# 전체 n회만큼 진행하면 되므로 while문은 안 써도 될 것
from collections import deque
from sys import stdin
input = stdin.readline


def bfs(idx):
    que = deque([idx])
    count = 0
    for _ in range(n):
        target = que.popleft()
        count += 1
        if array[target] == k:
            return count
        que.append(array[target])
    return -1


n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
visited = [0] * (n + 1)
print(bfs(0))

