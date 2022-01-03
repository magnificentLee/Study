from sys import stdin
input = stdin.readline

n = input().rstrip()
target = input().rstrip()
l = len(target)
idx = 0
count = 0
while idx < len(n):
    if n[idx:idx + l] == target:
        count += 1
        idx += l
    else:
        idx += 1
print(count)

# 파이썬에서 가능한 방법
"""
n = input()
target = input()
print(n.count(target))
"""