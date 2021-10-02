# 출력결과를 보면 중복을 판단할 필요가 없음
# 따라서 중복체크를 제거해보자
n, m = map(int, input().split())
number_list = [i + 1 for i in range(n)]
arr = []


def DFS(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(number_list[i])

        DFS(x + 1)
        arr.pop()

DFS(0)