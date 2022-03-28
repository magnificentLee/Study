# 백준 2567번
# 다른 bfs와 다른점은 [ny][nx] 위치로 이동하는게 아닌 0인지 체크만 해주는 것
# 만약 array[j][i]가 1일 때 4방향 체크하면서 체크한 위치가 0이라면 결과 +1
# 모서리 부분은 어차피 4방향을 체크하므로 문제 없을것임
n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[j][i] = 1
for i in range(101):  # 전체 배열 체크
    for j in range(101):  # 전체 배열 체크
        if array[j][i] == 1:  # 현재 위치가 1일때 진행(색종이 부분은 1이므로)
            for idx in range(4):  # 상우하좌 체크
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0 <= nx <= 100 and 0 <= ny <= 100 and array[ny][nx] == 0:  # 경계를 벗어나지 않으면서 다음위치가 0이라면
                    result += 1
print(result)
