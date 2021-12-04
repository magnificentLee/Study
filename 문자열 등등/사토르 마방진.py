# ABC
# BDF
# CFG
# 와 같이 1행123열, 1열123행 이 서로 같은 방식이 사토르 마방진이다
from sys import stdin
input = stdin.readline
n = int(input())
array = [input() for _ in range(n)]
flag = 1
for i in range(n):
    for j in range(n):
        if array[i][j] != array[j][i]:
            flag = 0
            break
if flag == 1:
    print("YES")
else:
    print("NO")