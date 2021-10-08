# 단순히 카운트 해버리는 방법은 출제자의 의도가 아닐것임
# 난이도가 브론즈1인 이유가 있을것
"""
n = int(input())
string = input()
print(string.count("pPAp"))
"""
# 문자열에서 pPAp 형태를 찾는 KMP 알고리즘 문제임 (블로그펌)
from sys import stdin
input = stdin.readline

n = int(input())
s = list(input())
result = 0
flag = 0
for i in range(n):
    if flag < 3 and s[i] == "p":
        flag = 1
    elif flag == 1 and s[i] == "P":
        flag = 2
    elif flag == 2 and s[i] == "A":
        flag = 3
    elif flag == 3 and s[i] == "p":
        result += 1
        flag = 0
    else:
        flag = 0
print(result)