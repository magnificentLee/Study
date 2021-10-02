h, m = map(int, input().split())
time = h * 60 + m - 45 # 24 00 = 1440
hour = time // 60
minute = time % 60
if time >= 0:
    print(hour, minute)
else:  # 음수의 나머지는 양수
    print(23, minute)