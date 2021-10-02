""" 1차, 이전 처럼 한 경우
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a + b)
////////////////////////////////////////
import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
113B / 1396ms
"""
"""
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
126B / 1432ms
"""
import sys
t = int(input())
for i in range(t):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))
# 113B / 1232ms
