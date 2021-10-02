"""
t = input()
ord_t = ord(t)
print(ord_t, chr(ord_t + 13))
결과 = B = O, a = n
따라서 ROT13 의 뜻은 입력된 문자를 아스키코드로 변환후 13을 더하고 문자로 변환한 값이라는뜻
"""
n = input()
n_list = []
for i in n:
    if i == " ":  # 공백의 경우만 따로 고려
        n_list.append(i)
        continue
    elif 65 <= ord(i) <= 90:  # 대문자의 경우
        if ord(i) >= 78:  # 중간값을 넘어갈 경우 -> Z를 초과하게 됨
            n_list.append(chr(ord(i) - 13))
        else:
            n_list.append(chr(ord(i) + 13))
    elif 97 <= ord(i) <= 122:  # 소문자의 경우
        if ord(i) >= 110:  # 중간값을 넘어갈 경우 -> z를 초과하게 됨
            n_list.append(chr(ord(i) - 13))
        else:
            n_list.append(chr(ord(i) + 13))
    else:  # 대소문자가 아닌 기호, 숫자를 고려
        n_list.append(i)
for j in n_list:
    print(j, end="")
"""
ord_e = ord(i) + 13
if ord_e > 90:  # Z = 90, A = 65
ord_re = ord_e - 90  # if 91이면 90(Z) + 1 = A(65)가 되야 하므로
n_list.append(chr(65 + ord_re - 1))  # 65 + 1 - 1 = 65 (A)
else:
n_list.append(chr(ord_e))
for i in n_list:
    print(i, end="")
"""