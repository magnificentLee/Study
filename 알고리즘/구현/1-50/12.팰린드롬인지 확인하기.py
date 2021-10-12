string = input()

if string == string[::-1]:
    print(1)
else:
    print(0)

# 초기작성
"""
string = input()
flag = 1
for i in range(len(string) // 2):
    if string[i] == string[-(i + 1)]:
        continue
    else:
        flag = 0
        break
if flag == 1:
    print(1)
else:
    print(0)
"""