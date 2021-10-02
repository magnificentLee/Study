# 시간초과
# 원인
# list와 큐/덱 은 근본적으로 걸리는 시간이 다르기 때문에 이러한 시간제한이 있는 문제에선
# list를 큐 또는 덱으로 사용하면 절대 안 됨
# list : O(N) 의 시간이, 덱은 O(1) 의 시간이 걸리기 때문
"""
import sys

n = [i for i in range(1, int(sys.stdin.readline()) + 1)]
while True:
    n.pop(0)
    if len(n) == 1:
        print(*n)
        break
    n.append(n.pop(0))
"""
# deque로 풀었으나 100%에서 런타임에러 발생
"""
import sys
from collections import deque

n = deque(i for i in range(1, int(sys.stdin.readline()) + 1))
while True:
    n.popleft()
    n.append(n.popleft())
    if len(n) == 1:
        print(*n)
        break
"""
# 원인 : 1을 넣을 경우 deque가 비어버리기 때문에 에러 발생
import sys
from collections import deque

n = deque(i for i in range(1, int(sys.stdin.readline()) + 1))
while len(n) > 1:
    n.popleft()
    n.append(n.popleft())
print(*n)
