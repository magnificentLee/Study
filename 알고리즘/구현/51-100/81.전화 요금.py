# 오늘 부터 = 00시부터, 오늘 까지 = 00시 전까지
result = 0
for _ in range(int(input())):
    n, time = input().split()
    time = int(time)
    clock = n.split(":")
    start_hour = int(clock[0])
    m = int(clock[1])
    end_m = m + time
    end_hour = start_hour
    if end_m >= 60:
        end_hour += 1
        end_m -= 60
    if end_hour >= 24:
        end_hour -= 24
    if 7 <= start_hour <= 18 and 7 <= end_hour <= 18:
        result += time * 10
    elif (0 <= start_hour <= 6 or 19 <= start_hour <= 23) and (0 <= end_hour <= 6 or 19 <= end_hour <= 23):
        result += time * 5
    elif start_hour == 18 and end_hour == 19:
        result += (60 - m) * 10 + end_m * 5
    elif start_hour == 6 and end_hour == 7:
        result += (60 - m) * 5 + end_m * 10
print(result)