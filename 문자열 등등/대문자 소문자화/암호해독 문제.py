# 백준 14584 암호 해독
# 97, 122 = a, z
import sys

code = sys.stdin.readline().rstrip()
words = [sys.stdin.readline().rstrip() for _ in range(int(input()))]
for j in range(26):
    result = ""
    for i in code:
        tmp = ((ord(i.upper()) - 97 + j) % 26) + 97
        result += chr(tmp)
    for i in words:
        if i in result:
            print(result)
            exit()