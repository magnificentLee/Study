# 예제를 보면 N = 2, 입력값은 10, 15 정렬하면 [15, 10]
# 1.15일때 15만 버틸 수 있음, 2.15,10 일 때 10*2 = 20 최대 20을 버팀
# if 10, 15, 1 이면 1*3=3 최대 3을 버티므로 15,10만 선택해야됨
from sys import stdin as st

t = int(input())
n = sorted([int(st.readline()) for _ in range(t)], reverse=True)
result = 0
for i in range(t):
    if result < n[i] * (i + 1):
        result = n[i] * (i + 1)
print(result)
