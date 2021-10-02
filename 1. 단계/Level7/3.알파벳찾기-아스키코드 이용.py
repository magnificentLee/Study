# 기존방법 : 알파벳 리스트를 만들어 치환하는 방법 68ms, 221B
"""
n = input()
alpha = list("abcdefghijklmnopqrstuvwxyz")
array = [-1 for i in alpha]

for i in range(len(n)):
    if array[alpha.index(n[i])] == -1:
        array[alpha.index(n[i])] = i
for j in array:
    print(j, end=" ")
"""
# 새로운방법 : 아스키코드를 이용하는 방법
"""
입력 조건에 주목
"첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다."
알파벳 소문자로 이루어져 있기 때문에 97~122 값을 이용하면 된다.
문자 to 코드 : ord
코드 to 문자 : chr
"""
# 68ms, 91B
n = input()
alpha = list(range(97, 123))
for i in alpha:
    print(n.find(chr(i)), end=" ")