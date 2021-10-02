""" 4(전체숫자) 3 3 3 3
3 - (1 - 1)  = 3
3 - (2 - 1)  = 2
3 - (3 - 1)  = 1
3 - (4 - 1)  = 0
result = 3 + 2 + 1 = 6
"""
# 손님의 순서를 바꿔 최대 팁을 얻는게 목표
# 팁이 높은 순서로 정렬해서 받는게 팁ㅋ(종이에 풀어보면 알 수 있음)
from sys import stdin
n = int(stdin.readline())
tips = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)
result = 0
for i in range(len(tips)):
    minus = (i + 1) - 1  # i = 0 부터 시작이라는걸 간과했었음
    plus = tips[i] - minus
    if plus < 0:
        plus = 0
    result += plus
print(result)