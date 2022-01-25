# 후기
# 구현하는데 심각하게 어려웠던 문제는 아니지만 문제 조건을 제대로 읽지 않아 정답 출력부분에 가서야 잘못된걸 알고 시간이 걸렸음
# 문제에 적혀있는 그림대로 구현하여 정답이 6,6이 아닌 0,5가 나왔었고 (인덱스+1을 해줘도 1,6 임)
# 내가 구현할 때 쓰는 방식과 달리 문제는 x,y 좌표대로 진행했기 때문에 (1,1 2,1 3,1....) 내가 예상한 답과 달랐다
# 마지막에 res1, res2의 위치를 바꿔서 출력했기 때문에 문제는 없었음

# i[dy][dx]  → ↓
# 달팽이 모양, ↑ ← 을 생각하자
# 어떻게 하면 중앙에서 멈출 수 있을까?
# 상하좌우를 탐색하여 방문처리 됐으면?
# 시작부터 1씩 늘어난다고 할 때 c * r 에서 1 * 1 = 1, 1 * 2 = 2.... c * r = total, 즉 c * r = total은
# 마지막 위치의 값일 것임

# 인덱스 때문에 구현자체는 시계 반대 방향으로 하자

# 마지막 인덱스 표현식에선 x, y의 위치가 서로 바뀐다 예를 들어 1,1 2,1 3,1 4,1...7,1(좌우) 이런식으로 진행됨
from sys import stdin
input = stdin.readline

c, r = map(int, input().split())
k = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
x, y, idx = 0, 0, 0  # 시작 지점에 주의, (1행 1열이 아니라 r행 0열임)

# 전체 확인용 배열
#array = [[0 for _ in range(c)] for _ in range(r)]
#array[0][0] = 1  # 시작지점 카운트처리

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
        #array[ny][nx] = count 전체 확인용 배열
    else:
        idx = (idx + 1) % 4
if count == k:
    print(res2, res1)  # 배열이 1,1 2,1 3,1 ... (좌우) 이런식으로 구현하라고 했기 때문에 마지막에 y, x값 위치를 바꿔줌
else:
    print(0)