def leap(y):  # 달력 계산
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:  # 윤년이면
        return True
    else:
        return False


def cal(y, m, d):
    num = 31
    if m in [4, 6, 9, 11]:
        num = 30
    if m == 2:
        if leap(y):  # 윤년이면
            num = 29
        else:
            num = 28
    if d > num:  # 달 증가, 일 초기화용 T/F
        return True
    else:
        return False


t = input().split()  # 입력 yyyy-mm-dd n일후 /ex) 2014-04-02 1
tmp = t[0].split("-")
n = int(t[1])
year, month, day = int(tmp[0]), int(tmp[1]), int(tmp[2])
for _ in range(n):
    day += 1
    if cal(year, month, day):
        month += 1
        day = 1
        if month > 12:
            year += 1
            month = 1
if day < 10:
    day = "0" + str(day)
if month < 10:
    month = "0" + str(month)
print("{}-{}-{}".format(year, month, day))