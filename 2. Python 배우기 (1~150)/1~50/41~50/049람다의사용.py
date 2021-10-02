"""
t = int(input())

for i in range(t):
    n = int(input())
    drink_list = []
    for j in range(n):
        name, drink = input().split()
        drink_list.append((name, int(drink)))
        drink_list.sort(key=lambda x: x[1])
    print(drink_list[-1][0])
"""
t = int(input())

for i in range(t):
    n = int(input())
    Max = 0
    mName = ""
    for j in range(n):
        name, num = input().split()
        num = int(num)
        if num > Max:
            Max = num
            mName = name
    print(mName)
