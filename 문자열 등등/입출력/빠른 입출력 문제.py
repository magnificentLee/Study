# 백준 1920 수 찾기
from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        stdout.write("1\n")
    else:
        stdout.write("0\n")