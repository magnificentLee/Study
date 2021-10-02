a = int(input("입력:"))
b = a - 20
if b < 0:
    print(0)
elif b > 255:
    print(255)
else:
    print(b)