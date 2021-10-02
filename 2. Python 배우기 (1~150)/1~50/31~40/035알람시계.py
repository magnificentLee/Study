h, m = map(int, input().split())
total_time = h * 60 + m - 45

hour = total_time // 60
minute = total_time % 60

if total_time >= 0:
    print(hour, minute)
else:
    hour = 23
    print(hour, minute)
""" 더 간단한 방법
h, m = map(int, input().split())
if m < 45:
    if h == 0:
        h += 23
    else:
        h -= 1
    print(h, m + 15)
else:
    print(h, m - 45)
"""