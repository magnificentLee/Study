t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room = n // h
    result = floor * 100 + room
    print(result)
# floor = h 가 정답이고 floor = n 이 정답이 아닌 이유
# 6 8 10, 6 8 6 에서도 정답이 나오지만 반례가 존재함
# 3 8 6 = 302가 정답이지만 602가 나옴