import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%s: %s"%(i, a + b))
#   152B / 64ms
""" 117B / 100ms
t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())
    print("Case #%s: %s"%(i, a + b))
"""