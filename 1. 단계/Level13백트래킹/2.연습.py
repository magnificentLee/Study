n, m = map(int, input().split())
n_list = [i + 1 for i in range(n)]
check_num = [False] * n
arr = []


def dfs(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        if check_num[i]:
            continue
        check_num[i] = True
        arr.append(n_list[i])

        dfs(x + 1)
        arr.pop()

        for j in range(i + 1, n):
            check_num[j] = False

dfs(0)