# 풀면서 꽤 재밌었던 문제, 나름 수월하게 풀었고 꽤 괜찮다고 생각했지만
# 채점 결과를 보니 더 좋은 코드가 많았음(메모리도 덜 먹고 속도도 더 빠르고)
# y축의 숫자를 역순의 for문을 만들어 대조 시켜 출력하는 것보다 더 좋은 방법이 없을까 고민해야되는 부분
n, m = map(int, input().split())
array = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# 문제의 시작지점은 좌하단 기준 0,0 이지만 현재 코드의 좌하단은 n,0 이기 때문에 역순으로 맞춰줌
array_y = [i for i in range(n, -1, -1)]
move_list = [input() for _ in range(m)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
y, x, idx = n, 0, 0
flag = 1
for i in range(m):
    a, b = move_list[i].split()
    b = int(b)
    if a == "MOVE":
        ny = y + dy[idx] * b
        nx = x + dx[idx] * b
        if ny < 0 or ny > n or nx < 0 or nx > n:
            flag = 0
            break
        else:
            y, x = ny, nx
    else:  # a == "TURN"
        if b == 0:
            idx = (idx + 1) % 4
        else:  # int(b) == 1:
            idx = (idx - 1) % 4
if not flag:
    print(-1)
else:
    print(x, array_y[y])
# 코드 완성후 보완한 부분
# 맵을 벗어나는 경우 입력값을 전부 받기전에 끝냈기 때문에 정상적으로 받기 위해 break문을 없앴다가
# 그 이후에 쓸 때 없이 시간을 낭비하는 것 같아 이동 명령어 리스트를 처음에 받은 이후
# 명령어 처리 과정에 리스트에서 꺼내오는 방식을 사용, break문도 다시 넣었음