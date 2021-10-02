""" 1차 시도
import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(n)
    n -= 1
"""
print('\n'.join(map(str,range(int(input()), 0, -1))))