# 64ms, 118B
import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split(","))
    print(a + b)
""" 76ms, 93B
t = int(input())

for i in range(t):
    a, b = map(int, input().split(","))
    print(a + b)
"""