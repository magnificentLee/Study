# 원으로 생각하자
# 각 좌표는 원의 중심, 거리는 반지름으로 생각
t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # distance : 원 위의 임의의 점까지 거리(원의 방정식)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 중심이 같은 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
        print(0)
    elif r1 == distance + r2 or r2 == distance + r1 or distance == r1 + r2:
        print(1)
    else:
        print(2)