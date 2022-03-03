# 연산에 필요한 최솟값을 구하는 문제
from collections import deque

a, b = map(int, input().split())  # a = 시작값, b = 목표값
q = deque([(a, 1)])  # 1 = 연산의 횟수(시작값)
result = -1  # 불가능 할 경우 -1 출력
while q:
    i, count = q.popleft()
    if i == b:
        result = count
        break
    if i * 2 <= b:
        q.append((i * 2, count + 1))
    tmp = int(str(i) + "1")
    if tmp <= b:
        q.append((tmp, count + 1))
print(result)