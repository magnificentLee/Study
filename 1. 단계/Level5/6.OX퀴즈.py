# 문제가 연속해서 맞을 경우 1점씩 늘어난다는 점에 주의할 것 OX = 1, XOOO = 3
number = int(input())

for i in range(number):
    num = input()
    num_list = list(num)
    sum = 0
    c = 1 # 점수 증가
    for i in num_list:
        if i == "O":
            sum += c
            c += 1 # 연속해서 맞을 경우 점수 증가 ex) 1 + 2 + 3
        else:
            c = 1 # 연속해서 맞지 못 할 경우 ex) 1 + 0 + 1
    print(sum)