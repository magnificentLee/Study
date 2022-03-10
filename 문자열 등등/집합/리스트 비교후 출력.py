# 백준 10815 숫자 카드
# 빠른 입출력을 이용한 방법
from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        stdout.write("1 ")
    else:
        stdout.write("0 ")
# 가장 빠른 방법
"""
from sys import stdin
input = stdin.readline

def solution():
    input()
    a = set(input().split())
    input()
    b = input().split()
    res = ""
    for i in b:
        if i in a:
            res += "1 "
        else:
            res += "0 "
    print(res)
solution()
"""