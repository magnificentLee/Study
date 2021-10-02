n = input()
alpha = list(range(97, 123))
for i in alpha:
    print(n.find(chr(i)), end=" ")
# chr : 문자 to 숫자
# find = 없으면 -1 있으면 인덱스로 변환