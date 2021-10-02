""" 62 B 72ms
n = int(input())

for i in range(1, n + 1):
    print("*" * i)
"""
import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    print("*" * i)
# 87B / 64ms