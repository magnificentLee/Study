""" 빠른 입력을 사용한 경우, 하지만 차이는 없었음 둘 다 64ms로 동일했음
import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(a // b, a % b))
"""
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(a // b, a % b))
