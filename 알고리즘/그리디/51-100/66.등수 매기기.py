# 예상 등수 : 1 1 2 3 5
# 실제 등수 : 1 2 3 4 5
# 절댓값차  : 0 1 1 1 0 = 합계 3
# 빠른 입력을 사용하지 않으면 시간초과가 발생함
from sys import stdin
input = stdin.readline

n = int(input())

grade = sorted([int(input()) for _ in range(n)])
result = 0
for i in range(n):
    result += abs(grade[i] - (i + 1))
print(result)