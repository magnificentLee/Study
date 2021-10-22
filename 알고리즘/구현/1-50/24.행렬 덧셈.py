# 복잡하게 생각X
# 입력 받는 값은 A의 원소 N개, B의 원소 M개이고 각 행의 값을 더하는 것
# n행 m열 이라는 점에서 실수 발생
# n행 n열로 반복문을 돌려서 오답이 발생했음
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
        print(a[i][j], end=" ")
    print()