# min, max의 사용
"""
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print("{} {}".format(min(a), max(a))) 128B / 476ms

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
print("{} {}".format(min(a), max(a))) 115B / 436ms

n = int(input())
a = list(map(int, input().split()))
print("{} {}".format(min(a), max(a))) 90B / 432ms

n = int(input())
a = list(map(int, input().split()))
print(min(a), max(a)) 74B / 472ms
"""
n = int(input())
a = list(map(int, input().split()))
print(f"{min(a)} {max(a)}") # 80B / 432ms
