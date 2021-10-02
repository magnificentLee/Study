a = input("주민등록번호: ").split("-")[1]
num = a[1:3]
if 0 <= int(num) <= 8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")
print(a, num)