# 마지막 플러그는 구멍을 전부 꽂을 수 있기 때문에 이것만 제외하는 식을 구하면
# total - (p - 1) :(p - 1)은 마지막 플러그를 제외한 꽂을 수 없는 구멍수
import sys

p = int(sys.stdin.readline()) # 플러그 갯수
total = 0
for i in range(p):
    n = int(sys.stdin.readline())
    total += n
print(total - (p - 1))
