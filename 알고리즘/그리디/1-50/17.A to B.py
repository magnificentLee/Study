# 입력값의 범위가 10**9 까지 가기 때문에 일반적인 방법으론 안 될것
from collections import deque

a, b = map(int, input().split())
result = -1
que = deque([(a, 1)])
while que:
    i, cnt = que.popleft()
    if i == b:
        result = cnt
        break
    if i * 2 <= b:
        que.append((i * 2, cnt + 1))
    if int(str(i) + "1") <= b:
        que.append((int(str(i) + "1"), cnt + 1))
print(result)