# 둘레의 길이를 구하는 문제
# bfs를 이용하되 nx, ny 위치로 이동하는게 아닌 체크만 해주는 방식
# array[j][i]가 1일 때 상좌하우 를 array[ny][nx]로 체크하여 만약 0이라면 둘레라는 뜻이므로 결과+1 4방향 체크후 다음 반복문 이동
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
for i in range(101):
    for j in range(101):
        if array[j][i] == 1:
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0 <= nx <= 100 and 0 <= ny <= 100 and array[ny][nx] == 0:
                    result += 1
print(result)
