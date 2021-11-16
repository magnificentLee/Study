# 처음 생각했던 방식
# 100 * n 만큼 전체 넓이를 구하고 x 값의 크기로 정렬후 겹치는 만큼 빼주는 것
# 다만 이렇게하면 n의 값이 커지고 겹치는 값이 많을 수록 복잡해질것임
"""
n = int(input())
total = 100 * n  # 사각형 하나당 넓이는 10*10 이기 때문
graph = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
print(graph)
"""
n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]  # 100 * 100 좌표계 생성
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1
result = 0
for i in array:
    result += sum(i)  # i = 리스트
print(result)