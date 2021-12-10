import datetime

y, m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())

today = datetime.date(y, m, d)  # 현재
target = datetime.date(y1, m1, d1)  # 목표
result = str(target - today).split()  # 목표 - 현재
# result 확인해본결과 1천년 차이 = 365243
if int(result[0]) >= 365243:
    print("gg")
else:
    print("D-%s" % result[0])