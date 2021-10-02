"""
t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
n.sort()
for i in n:
    print(i)
"""
import sys

t = int(input())
n = []
for _ in range(t):
    n.append(int(sys.stdin.readline()))
n.sort()
for i in n:
    print(i)
