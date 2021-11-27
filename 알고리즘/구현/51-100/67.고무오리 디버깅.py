n = input()
flag = 0
if n == "고무오리 디버깅 시작":
    while True:
        string = input()
        if string == "고무오리 디버깅 끝":
            break
        if string == "문제":
            flag += 1
        elif string == "고무오리":
            flag -= 1
            if flag < 0:
                flag += 3  # flag = -1 일 떄 2 문제 추가 (flag = 2)되야 하므로
if flag == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")
