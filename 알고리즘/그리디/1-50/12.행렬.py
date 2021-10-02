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
            a[i][j] = 1 - a[i][j]  # 뒤집기

# 3 * 3 행렬의 왼쪽 상단 지점을 기준으로 삼는다
for i in range(0, n - 2):  # 0 ~ n - 3
    for j in range(0, m - 2):  # 0 ~ m - 3
        if a[i][j] != b[i][j]:
            result += 1
            solve(i, j)

if search():
    print(result)
else:
    print(-1)