n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

# result 를 더해가는 방식
result = 0

# 틀린 부분 찾기
def search():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

# 틀린 부분 고치기
def solve(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j] # 뒤집기

# 본문
for i in range(0, n - 2):
    for j in range(0, m - 2):
        if a[i][j] != b[i][j]:
            result += 1
            solve(i, j)

if search():
    print(result)
else:
    print(-1)