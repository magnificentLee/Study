"""
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])
print(result)
"""
"""
from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0
for i in combinations(card, 3):
    temp_sum = sum(i)
    if max_sum < temp_sum <= m:
        max_sum = temp_sum
print(max_sum)
"""
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])
print(result)