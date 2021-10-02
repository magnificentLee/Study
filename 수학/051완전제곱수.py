# 8^2 = 64, 9^2 = 81, 10^2 = 100 즉, 어떤 정수를 제곱하여 만들어지는 수
"""
m = int(input())
n = int(input())
a = 1
a_list = []
while True:
    b = a ** 2
    if b > n:
        break
    elif b > m:
        a_list.append(b)
    a += 1
if len(a_list) >= 1:
    print(sum(a_list), min(a_list), sep="\n")
else:
    print(-1)
"""
m = int(input())
n = int(input())
a = 1
a_list = []
while True:
    b = a ** 2
    if b > n:
        break
    elif b >= m:  # b > m 으로 할 경우 10000~10000 의 경우가 -1로 나옴
        a_list.append(b)
    a += 1
if len(a_list) >= 1:
    print(sum(a_list), min(a_list), sep="\n")
else:
    print(-1)