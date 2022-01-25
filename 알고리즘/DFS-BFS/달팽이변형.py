# 백준 10157 자리배정 문제

from sys import stdin
input = stdin.readline

c, r = map(int, input().split())
k = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x, y, idx = 0, 0, 0  # 시작 지점에 주의, (1행 1열이 아니라 r행 0열임)

# 전체 확인용 배열
array = [[0 for _ in range(c)] for _ in range(r)]  # 전체 배열 확인용, 정답에 아무 상관 없음
array[0][0] = 1  # 위 배열의 시작지점 카운트처리, 정답에 아무 상관 없음

visited = [[0 for _ in range(c)] for _ in range(r)]  # 1...7(c = 좌우)
visited[0][0] = 1  # 시작지점 방문처리
count = 1  # 시작지점 카운트처리
total = c * r
res1, res2 = 0, 0
while True:
    if count == total or count == k:  # 시작지점에 count == k를 둔 이유는 1,1 일때 0이 나오기 때문에 바꿨음
        res1, res2 = y + 1, x + 1  # 인덱스라서 +1
        break
    ny = y + dy[idx]
    nx = x + dx[idx]

    if 0 <= ny < r and  0 <= nx < c and visited[ny][nx] == 0:
        visited[ny][nx] = 1
        count += 1
        y, x = ny, nx
        array[ny][nx] = count # 전체 확인용 배열, 정답에 아무 상관 없음
    else:
        idx = (idx + 1) % 4
if count == k:
    print(res2, res1)  # 배열이 1,1 2,1 3,1 ... (좌우) 이런식으로 구현하라고 했기 때문에 마지막에 y, x값 위치를 바꿔줌
else:
    print(0)
# 전체 확인용 배열 출력
for i in array:
    print(i, sep=" ")
# 입력값
# 7 6    7 6
# 11     87
# 출력값
# 6 6    0
