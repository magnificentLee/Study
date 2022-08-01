# 풀이법2: dfs로 푸는법, 규칙을 이용하는법

def dfs(node, res):
    visited[node] = 1
    for i in array[node]:
        if not visited[i]:
            res = dfs(i, res + 1)
    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        array[a].append(b)
        array[b].append(a)
    visited = [0] * (n + 1)
    result = dfs(1, 0)
    print(result)

# 모든 국가가 연결됐기 때문에 n - 1 로도 결과가 나옴
"""
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
    print(n - 1)
"""