# 단순 bfs 문제
# 이동 가능한 방향이 우, 하 밖에 없음
from collections import deque

def bfs(y, x):
    que = deque()
    que.append((y, x, array[y][x]))
    dy = [0, 1]
    dx = [1, 0]  # a[y][x], x축 이동값
    while que:
        y, x, l = que.popleft()
        for i in range(2):
            ny = y + dy[i] * l
            nx = x + dx[i] * l
            if 0 <= ny < n and 0 <= nx < n and l != 0:
                if ny == nx == n - 1:
                    return True
                que.append((ny, nx, array[ny][nx]))
    return False

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")