#  76ms, 400B
import sys

t = int(input())

for i in range(t):
    p, m = map(int, sys.stdin.readline().split())
    n_list = []
    count = 0
    for j in range(p):
        n_list.append(int(sys.stdin.readline()))
    if m == 1:
        print(p - 1)
    else:
        count = 0
        for k in range(1, m + 1):
            if n_list.count(k) > 1:
                count += n_list.count(k) - 1
        print(count)
""" 168ms, 362B
t = int(input())

for i in range(t):
    p, m = map(int, input().split())
    n_list = []
    count = 0
    for j in range(p):
        n_list.append(int(input()))
    if m == 1:
        print(p - 1)
    else:
        count = 0
        for k in range(1, m + 1):
            if n_list.count(k) > 1:
                count += n_list.count(k) - 1
        print(count)
"""