# 백준 2606 바이러스
# DFS 혹은 BFS 구현 문제
# 다음은 DFS코드
t = int(input())
n = int(input())
array = [[] for _ in range(t + 1)]
visited = [0] * (t + 1)
for _ in range(n):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)
result = 0
def dfs(idx):
    global result
    visited[idx] = 1
    for i in array[idx]:
        if not visited[i]:
            dfs(i)
            result += 1
dfs(1)
print(result)