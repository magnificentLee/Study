def check(n, flag):
    l = len(n)
    array = ["a", "e", "i", "o", "u"]
    ex = ["e", "o"]
    v_count = 0
    # consonant 자음, vowel 모음, continuity 연속성
    c, v = 0, 0  # 자.모 3연속 확인, 같은 글자 2연속 확인
    pre_idx = ""
    for i in range(l):
        if n[i] in array:  # 모음일 때
            v_count += 1
            v += 1
            c = 0
            if v >= 3:
                flag = 0
            if pre_idx == n[i]:
                if n[i] in ex:
                    pass
                else:
                    flag = 0
        else:  # 자음일 때
            c += 1
            v = 0
            if c >= 3:  # 자음이 3연속으로 나오면
                flag = 0
            if pre_idx == n[i]:  # 같은게 2연속으로 나오면
                flag = 0
        pre_idx = n[i]
    if v_count < 1:
        flag = 0
    return flag


while True:
    n = input()
    if n == "end":
        break
    result = check(n, 1)
    if result == 1:
        print("<%s> is acceptable." % n)
    else:
        print("<%s> is not acceptable." % n)