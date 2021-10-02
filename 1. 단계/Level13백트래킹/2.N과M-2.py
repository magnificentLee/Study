n, m = map(int, input().split())
n_list = [i + 1 for i in range(n)]
check_number = [False] * n
array = []


def DFS(x):
    if x == m:
        print(*array)
        return
    for i in range(n):
        if check_number[i]:
            continue
        array.append(n_list[i])
        check_number[i] = True
        DFS(x + 1)
        array.pop()

        for j in range(i + 1, n):
            check_number[j] = False

DFS(0)