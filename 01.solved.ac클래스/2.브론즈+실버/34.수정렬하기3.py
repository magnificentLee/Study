# 메모리 초과
# 문제 조건을 제대로 보지 않았기 때문에 발생
"""
import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))
result.sort()
print(*result, sep="\n")
"""
import sys

t = int(sys.stdin.readline())

num = [0] * 10001
for _ in range(t):
    num[int(sys.stdin.readline()) - 1] += 1
for i in range(10001):  # range 1, 10001 / print(i) 로 할 경우 틀림
    [print(i + 1) for _ in range(num[i])]