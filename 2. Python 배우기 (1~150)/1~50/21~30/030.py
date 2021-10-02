""" 1차 성공
while True:
    a, b = map(int, input().split())
    if a > b:
        print("Yes")
    elif a <= b or a >= b:
        if a == 0 and b == 0:
            break
        else:
            print("No")
"""
# 2차, 간결하게
a, b = map(int, input().split())

while not (a == 0 and b == 0):
    if a > b:
        print("Yes")
    else:
        print("No")
    a, b = map(int, input().split())
