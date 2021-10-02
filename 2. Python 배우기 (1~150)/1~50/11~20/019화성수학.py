"""
def calc(num, item):
    if item == "@":
        return num * 3
    elif item == "%":
        return num + 5
    elif item == "#":
        return num - 7


t = int(input())

for i in range(t):
    str_list = input().split()
    num = float(str_list.pop(0)) # pop(0) : 계산 숫자만 리스트 제외, 리스트 나머진 계산식
    for j in str_list:
        num = calc(num, j)
    print("%.2f" % num)
"""
# @ = *3, % = +5, # = -7


def calc(num, item):
    if item == "@":
        return num * 3
    elif item == "%":
        return num + 5
    elif item == "#":
        return num - 7


t = int(input())

for i in range(t):
    str_list = input().split()
    num = float(str_list.pop(0))
    for j in str_list:
        num = calc(num, j)
    print("%.2f" % num)
