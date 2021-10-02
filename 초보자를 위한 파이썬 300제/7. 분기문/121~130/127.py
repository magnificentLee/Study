a = input("주민등록번호: ").split("-")[1]
num = a[0]
if num in ["1", "3"]:
    print("남자")
elif num in ["2", "4"]:
    print("여자")
else:
    print("오류발생")