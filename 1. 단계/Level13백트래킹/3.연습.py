n, m = map(int, input().split())
n_list = [i + 1 for i in range(n)]
arr = []

def dfs(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(n_list[i])

        dfs(x + 1)
        arr.pop()

dfs(0)