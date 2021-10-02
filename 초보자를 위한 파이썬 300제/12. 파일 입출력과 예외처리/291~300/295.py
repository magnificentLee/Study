f = open("C:/users/extra/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip() # \n 제거 라는데 이해불가
    key, value = line.split()
    data[key] = value

print(data)
f.close()