a, b = map(int, input().split())

time = a * 60 + b - 45

if time > 1440:
    a = 0  # 시간은 0시로
    print(a, time % 60)
elif time < 0:
    a = 23
    print(a, time % 60)
else:
    print(time // 60, time % 60)
