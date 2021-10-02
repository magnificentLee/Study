# 1564ms 128B
"""
import sys

t = int(input())
n = []
for _ in range(t):
    n.append(int(sys.stdin.readline()))
n.sort()  # 시간복잡도 O(nlogn)
for i in n:
    print(i)
"""
# system input, system output 을 사용하는 방법
# 1496ms 149B
import sys
t = int(input())
n = []
for _ in range(t):
    n.append(int(sys.stdin.readline()))
for i in sorted(n):
    sys.stdout.write(str(i) + "\n")