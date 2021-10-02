import sys
t = int(input())
n = list(map(int, sys.stdin.readline().split()))
print(min(n), max(n))