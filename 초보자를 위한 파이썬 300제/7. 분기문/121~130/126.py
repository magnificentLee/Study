num = input("우편번호: ")
a = num[:3]
if a in ["010", "011", "012"]:
    print("강북구")
elif a in ["013", "014", "015"]:
    print("도봉구")
else:
    print("노원구")