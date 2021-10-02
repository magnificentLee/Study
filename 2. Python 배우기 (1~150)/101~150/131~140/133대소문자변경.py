lang = input()
lang_list = []
for i in lang:
    if i.isupper():
        lang_list.append(i.lower())
    elif i.islower():
        lang_list.append(i.upper())
for i in lang_list:
    print(i, end="")
""" 더 간단한 방법: i.swapcase()를 이용하는 방법
a = input()
a = a.swapcase()  # 대문자 to 소문자 / 소문자 to 대문자
print(a)
"""