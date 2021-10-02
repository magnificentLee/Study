# 시간이 너무 느림, 방법은?
# 조건 1 < L < P < V
from sys import stdin

n = 1
while True:
    l, p, v = map(int, stdin.readline().split())
    result = 0
    if l == 0:
        break
    result += (v // p) * l
    result += min(v % p, l)
    print("Case {}: {}".format(n, result))
    n += 1