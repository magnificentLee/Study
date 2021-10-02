"""1차 시도, 한눈에 알아보기 어려움
a, b = int(input()), int(input())
if a>0 and b>0: print(1)
elif a>0 and b<0: print(4)
elif a<0 and b>0 : print(2)
else: print(3)
"""
"""2차 시도, 알아보기 쉬움, 원점까지 포함한 경우
x, y = int(input()), int(input())
if x>0:
    if y>0:print(1)
    else: print(4)
elif x<0:
    if y>0:print(2)
    else: print(3)
else: print('원점')
"""
x, y = int(input()), int(input())
if x>0:
    if y>0:print(1)
    else: print(4)
else:
    if y>0:print(2)
    else: print(3)