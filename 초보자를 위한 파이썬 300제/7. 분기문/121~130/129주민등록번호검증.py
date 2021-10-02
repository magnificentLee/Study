a = input("주민등록번호: ")
total = int(a[0])*2 + int(a[1])*3 + int(a[2])*4 + int(a[3])*5 + \
        int(a[4])*6 + int(a[5])*7 + int(a[7])*8 + int(a[8])*9 + \
        int(a[9])*2 + int(a[10])*3 + int(a[11])*4 + int(a[12])*5
b = 11 - (total % 11)
if a[-1] == str(b):
    print("유효")
else:
    print("유효하지 않음")
print(total, b, a, a[-1]) # 검증용