# 아스키 코드를 이용하면 될 것
# 대문자 : 65~90, 소문자:97~122
string = input()
list1 = range(65, 91)
list2 = range(97, 123)
result = []
for i in range(len(string)):
    a = ord(string[i])
    if a in list1:
        a += 13
        if a > 90:
            a = a - 90 + 64
    elif a in list2:
        a += 13
        if a > 122:
            a = a - 122 + 96
    result.append(chr(a))
print(*result, sep="")
