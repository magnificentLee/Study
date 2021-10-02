# 산술평균
def mean(n):
    return round(sum(n) / len(n))
# 중앙값
def median(n):
    return n[len(n) // 2]
# 범위
def scope(n):
    return max(n) - min(n)
# 최빈값
import sys
from collections import Counter
def mode(n):
    if t == 1:
        return n[0]
    m = Counter(n).most_common(2)
    if m[0][1] == m[1][1]:
        return m[1][0]
    else:
        return m[0][0]

t = int(sys.stdin.readline())
n = sorted([int(sys.stdin.readline()) for _ in range(t)])
print(mean(n), median(n), mode(n), scope(n), sep="\n")
