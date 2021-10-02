# 64ms, 142B
import sys

t = int(input())

for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    n.sort(reverse=True)
    print(n[2])

""" 164ms, 117B
t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    print(n[2])
"""