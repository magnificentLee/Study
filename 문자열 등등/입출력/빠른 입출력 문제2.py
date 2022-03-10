# 백준 10815 숫자 카드
# 빠른 입력을 이용한 경우 : 112652kb, 3508ms
"""
from sys import stdin
input = stdin.readline

def binary(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a[mid] == target:
        return 1
    elif a[mid] > target:
        return binary(target, start, mid - 1)
    else:
        return binary(target, mid + 1, end)


n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    print(binary(i, 0, n - 1), end=" ")
"""
# 빠른 입출력을 이용한 경우 : 123652kb, 516ms
"""
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
"""
# 가장 빠른 방법 : 122620kb 432ms
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