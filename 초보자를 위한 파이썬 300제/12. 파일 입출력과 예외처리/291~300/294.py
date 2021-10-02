# 이미 있는 내용을 리스트에 저장하는것
f = open("C:/users/extra/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines() # python list

codes = []
for i in lines:
    code = i.strip() # \n
    codes.append(code)

print(codes)

f.close()