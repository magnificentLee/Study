""" 시간 160ms
t = int(input())

for i in range(1, t + 1):  # Case 1~5 까지 출력하기 위함
    a, b = map(int, input().split())
    print("Case {}: {}".format(i, a + b))
"""
# 빠른입력을 사용한 경우, 68ms 약 2.5배 빨라짐
import sys

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case {}: {}".format(i, a + b))
