n, m = map(int, input().split())
number_list = [i + 1 for i in range(n)]
check_number = [False] * n
arr = []
def DFS(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        if check_number[i]:
            continue

        arr.append(number_list[i])
        DFS(x + 1)
        check_number[i] = True
        arr.pop()
        for j in range(i + 1, n):
            check_number[j] = False

DFS(0)