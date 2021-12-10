# if [4 6 9 11] num = 30
def leap(y):  # 윤년 판별식
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False

def cal(y, m):
    num = 31
    if m in [4, 6, 9, 11]:
        num = 30
    if m == 2:
        if leap(y):
            num = 29
        else:
            num = 28
    return num


while True:
    day, month, year = map(int, input().split())
    count = 0
    if day == 0:
        break
    for i in range(1, month):
        count += cal(year, i)
    print(count + day)