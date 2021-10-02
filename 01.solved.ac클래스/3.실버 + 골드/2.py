# bfs로 만약 값이 1이면 주변 값을 확인해서 1인 값을 0으로 바꿔준다
# bfs를 실행시킬 때 마다 cnt 값을 증가, 마지막 cnt를 출력
# 상 하 좌 우  ; 좌표의 x(좌우), y(상하) 라고 생각X
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            k = a + dx[i]
            l = b + dy[i]
            # 맵의 한계 부여
            if k >= 0 and l >= 0 and k < n and l < m and maps[k][l] == 1:
                maps[k][l] = 0
                queue.append([k, l])


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())  # 열, 행, 1의 개수
    maps = [[0] * m for _ in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())  # a:열,b:행
        maps[b][a] = 1
    for k in range(n):
        for l in range(m):
            if maps[k][l] == 1:
                bfs(k, l)
                maps[k][l] = 0
                cnt += 1
    print(cnt)
