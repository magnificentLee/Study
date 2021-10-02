# 4492ms 379B
"""
t = int(input())
stack = []
plus_minus = []
count = 1
temp = True
for _ in range(t):
    n = int(input())
    while count <= n:  # push * 4 : 1 2 3 4 / pop * 2 : 4 3
        stack.append(count)
        plus_minus.append("+")
        count += 1
    if stack[-1] == n:
        stack.pop()
        plus_minus.append("-")
    else:
        temp = False
if not temp:
    print("NO")
else:
    print(*plus_minus, sep="\n")
"""
# 192ms 415B
import sys
t = int(sys.stdin.readline())
stack = []
plus_minus = []
count = 1
temp = True
for _ in range(t):
    n = int(sys.stdin.readline())
    while count <= n:
        stack.append(count)
        plus_minus.append("+")
        count += 1
    if stack[-1] == n:
        stack.pop()
        plus_minus.append("-")
    else:
        temp = False
if not temp:
    print("NO")
else:
    print(*plus_minus, sep="\n")