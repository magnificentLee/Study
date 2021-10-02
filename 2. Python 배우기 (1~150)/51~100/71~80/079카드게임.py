""" 빠른입력을 사용한 경우
import sys

total = 0
for i in range(5):
    a = int(sys.stdin.readline())
    total += a
print(total)
"""
total = 0
for i in range(5):
    a = int(input())
    total += a
print(total)