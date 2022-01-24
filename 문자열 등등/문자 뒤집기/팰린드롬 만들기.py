# 백준 1213
# 팰린드롬 : 앞뒤로 똑같은 문자
name = input()
alp = [0] * 26
flag = 0
left = ""
center = ""
for i in set(name):
    idx = ord(i) - 65
    alp[idx] += name.count(i)
for i in range(26):
    if alp[i] % 2 != 0:
        flag += 1
        center += chr(i + 65)
    left += chr(i + 65) * (alp[i] // 2)
    if flag > 1:
        break
right = left[::-1]
if flag > 1:
    print("I'm Sorry Hansoo")
else:
    print(left + center + right)
