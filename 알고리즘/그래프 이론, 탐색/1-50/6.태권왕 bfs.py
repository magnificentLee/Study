# 백준 14562 태권왕
# deque로 풀면 될듯? : bfs
# 죽음의 게임과 다른점은 최대 횟수를 알 수 없기 때문에 while문을 사용한다는점
# 무조건 정답이 나온다고 가정
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(s, t):
    count = 0
    que = deque([[s, t, count]])
    while que:
        left, right, count = que.popleft()
        if left < right:
            que.append([left * 2, right + 3, count + 1])
            que.append([left + 1, right, count + 1])
        elif left == right:
            break
    return count


c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t))
