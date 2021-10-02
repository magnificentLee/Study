"""
import sys

n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += i - table[j][k]
            else:
                max += table[j][k] - i
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
        ans = time
        height = 1
    print(ans, height)
"""
from sys import stdin
from collections import Counter

input = stdin.readline

def minecraft(g, b):
    gg = Counter(g)
    ret = []

    for h in range(max(gg.keys()), -1, -1):
        gt = 0
        inventory = 0
        needed = 0
        for gh, gc in gg.items():
            if h < gh:
                inventory += (gh - h) * gc
                gt += 2 * (gh - h) * gc
            elif h > gh:
                needed += (h - gh) * gc
                gt += (h - gh) * gc
        if inventory >= needed:
            ret.append([gt, h])
    ret.sort(key=lambda x: (x[0], -x[1]))
    return ret[0]

if __name__ == "__main__":
    n, m, b = map(int, input().split())
    grounds = []
    for _ in range(n):
        grounds.extend(list(map(int, input().split())))
    res = minecraft(grounds, b)
    print(res[0], res[1])