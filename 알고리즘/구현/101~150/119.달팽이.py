# 아이디어 자체는 빨리 생각났지만 구현하는데 시간이 좀 걸렸음
# 처음에 2중 for문으로 진행했다가 제대로 작동하지 않아 블로그를 참고, while문 + for문으로 바꿨음
# 시작 : 아래로, 방문했거나 경계일경우 방향 전환
# 아래, 오른쪽, 위, 옆 의 반복
n = int(input())
target = int(input())
dx = [0, 1, 0, -1]  # x 축 : i
dy = [1, 0, -1, 0]  # y 축 : j
count = n ** 2 - 1
start = count + 1
array = [[start for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited[0][0] = 1  # 시작지점을 방문처리 하지 않으면 무한루프에 걸림
tmp = 1  # 누적된 값을 빼게끔
x, y, idx = 0, 0, 0
res1, res2 = 1, 1  # 없을 경우 ↓
# n=4, target=16 일 때 즉, 시작지점에 있을 경우 nameError 가 발생함(res1, res2 값을 찾을 수 없기 때문)
# 아래 while문은 시작지점 다음부터 탐색하기 때문
while True:
    if count <= 0:
        break
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
        visited[ny][nx] = 1
        array[ny][nx] -= tmp
        tmp += 1
        count -= 1
        x, y = nx, ny
        if array[ny][nx] == target:
            res1, res2 = ny + 1, nx + 1  # 인덱스이기 때문에
    else:
        idx = (idx + 1) % 4
for i in array:
    print(*i)
print(res1, res2)