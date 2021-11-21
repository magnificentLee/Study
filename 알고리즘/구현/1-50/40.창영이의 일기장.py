# 성공했던 방법
# 모음직후 p + 모음이 나오므로 모음 인덱스 +3 부터 원래 문자가 나올것
string = input()
alp = ["a", "e", "i", "o", "u"]
result = ""
idx = 0
while True:
    result += string[idx]
    if string[idx] in alp:
        idx += 3
    else:
        idx += 1
    if idx >= len(string):
        break
print(result)
# 처음 시도했던 방식
# for문에서 i값이 초기화 되는 문제가 있어 while문으로 고쳐야 될 듯
"""
string = input()
alp = ["a", "e", "i", "o", "u"]
result = ""
for i in range(len(string)):
    result += string[i]
    print(i, string[i], end=" ")
    if string[i] in alp:
        i += 2
    if i >= len(string):
        break
print(result)
"""
# 제일 간단한 방법 : 블로그 참고
"""
s, p, i = input(), "aeiou", 0
while i < len(s):
    print(s[i], end='')
    if p.find(s[i]) > - 1:
        i += 2
    i += 1
"""