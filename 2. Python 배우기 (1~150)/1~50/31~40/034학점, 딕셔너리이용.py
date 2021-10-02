""" 첫시도, IndexError 발생
n = input()
a = n[0]
b = n[1]
if a == "A":
    if b == "+":
        print(4.3)
    elif b == "0":
        print(4.0)
    else:
        print(3.7)
elif a == "B":
    if b == "+":
        print(3.3)
    elif b == "0":
        print(3.0)
    else:
        print(2.7)
elif a == "C":
    if b == "+":
        print(2.3)
    elif b == "0":
        print(2.0)
    else:
        print(1.7)
elif a == "D":
    if b == "+":
        print(1.3)
    elif b == "0":
        print(1.0)
    else:
        print(0.7)
else:
    print(0.0)
"""
# 딕셔너리를 사용하기로 함
grade = {"A+": 4.3, "A0": 4.0, "A-": 3.7,
         "B+": 3.3, "B0": 3.0, "B-": 2.7,
         "C+": 2.3, "C0": 2.0, "C-": 1.7,
         "D+": 1.3, "D0": 1.0, "D-": 0.7,
         "F": 0.0}

score = input()
print(grade[score])