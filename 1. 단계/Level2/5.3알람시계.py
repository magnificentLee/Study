h, m = map(int, input().split())
total_time = h * 60 + m - 45

hour = total_time // 60
minute = total_time % 60

if total_time >= 0:
    print(hour, minute)
else:
    hour = 23
    print(hour, minute)