a_list = []
b_list = []

for i in range(10):
    a_list.append(int(input()))

for a in a_list:
    b = a % 42
    if b in b_list:
        pass  # 숫자 중복 방지
    else:
        b_list.append(b)

print(len(b_list))  # len : 문자열의 글자수를 구함
