# 킹, 돌을 둘 다 움직여야 함
# 다음 위치를 갈 수 없으면 다음 이동으로 건너감
# 만약 킹과 돌이 a8 a6에서 시작하여 T T B 을 실시할 경우
# a8 a7 / a8 a7 / a7 a6 이 됨
# 자동으로 경로를 찾아가는 문제가 아님에 주의
# 반복문을 통해 각각의 이동 경로를 입력 받음
# n[dy][dx]
k, r, n = input().split()  # 킹의 위치, 돌의 위치, 움직이는 횟수

dy = [1, 1, 0, -1, -1, -1, 0, 1]  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
dx = [0, 1, 1, 1, 0, -1, -1, -1]  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
move = {"T": 0, "RT": 1, "R": 2, "RB": 3, "B": 4, "LB": 5, "L": 6, "LT": 7}  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
alp = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
alpx = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
ky, kx = int(k[1]) - 1, alp[k[0]]  # 인덱스라 -1
ry, rx = int(r[1]) - 1, alp[r[0]]  # 인덱스라 -1
for i in range(int(n)):
    idx = move[input()]
    ny = ky + dy[idx]
    nx = kx + dx[idx]

    if 0 <= ny <= 7 and 0 <= nx <= 7:
        my = ry + dy[idx]  # next rock position y
        mx = rx + dx[idx]  # next rock position x
        if ny == ry and nx == rx:  # 만약 킹의 다음 위치가 현재 돌의 위치와 같다면
            if 0 <= my <= 7 and 0 <= mx <= 7:  # 돌의 위치가 체스판을 벗어나지 않을 때
                ry = my  # 돌을 다음 위치로 이동
                rx = mx
            else:
                continue
        # 킹의 다음 위치와 돌의 현재 위치와 같지 않다면
        ky = ny  # 킹을 다음 위치로 이동
        kx = nx
    else:
        continue
print(alpx[kx] + str(ky + 1))
print(alpx[rx] + str(ry + 1))
