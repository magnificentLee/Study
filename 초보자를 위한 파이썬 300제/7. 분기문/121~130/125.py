#a, b, c = input("휴대전화 번호 입력: ").split("-")
a = input("휴재전화 번호 입력: ").split("-")[0] #도 가능
if a == "011":
    print("SKT")
elif a == "016":
    print("KT")
elif a == "019":
    print("LGU")
else:
    print("알수없음")
