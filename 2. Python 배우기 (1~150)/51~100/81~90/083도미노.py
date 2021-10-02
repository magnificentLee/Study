""" 시간초과
# 최대 갯수는 2 = 2^2 개, 3 = 3^3 개, 따라서 n^n 개
n = int(input())
total = 0
for i in range(n**n + 1):
    total += i
print(total + n)
"""
# 도미노를 옆으로 엎으면 괄호로 나타낼 수 있다
# (0,1), (0,2), (1,1), (1,2), (2,2)
# 2중 for 문으로 해결할 수 있을 것.
n = int(input())
total = 0
for i in range(n + 1):
    for j in range(i, n + 1):
        total += i + j
print(total)
""" 진행과정
i = 0 일 때
j = 0, total = 0 / j = 1, total = 1/ j = 2, total = 3
i = 1 일 때
j = 1, total = 5/ j = 2, total = 8
i = 2 일 때
j = 2, total = 12
output
12
"""