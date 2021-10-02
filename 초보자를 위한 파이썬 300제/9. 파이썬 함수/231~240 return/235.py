def convert_int(string):
    num = int(string.replace(",", ""))
    return num


print(convert_int("1,234,567"))
# split은 리스트로 만들기 때문에 replace를 사용할것