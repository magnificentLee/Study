# 행렬 변환 : 3 * 3 크기의 행렬내 원소를 전부 뒤집는것
n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

result = 0


def search():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


def solve(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


for i in range(0, n - 2):
    for j in range(0, m - 2):
        if a[i][j] != b[i][j]:
            solve(i, j)
            result += 1
if search():
    print(result)
else:
    print(-1)