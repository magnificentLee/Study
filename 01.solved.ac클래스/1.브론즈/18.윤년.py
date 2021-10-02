# 조건을 잘 볼 것
# 4의 배수이면서(and) 100의 배수가 아닐 때 또는(or)
# 400의 배수일 때
n = int(input())

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(1)
else:
    print(0)