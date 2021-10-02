# 계속해서 최소값을 불러와주는 작업을 거쳐야하므로 우선순위 큐 자료구조를 사용하면됨
# 파이썬에서 우선순위 큐(priorityQueue) = heapq 모듈
from sys import stdin
import heapq
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    ch = list(map(int, stdin.readline().split()))
    result = 0
    queue = []
    for i in ch:
        heapq.heappush(queue, i)
    while len(queue) > 1:
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        result += a + b
        heapq.heappush(queue, a + b)
    print(result)
# 참고로 이 방식을 사용해도 183308KB, 5396ms의 시간복잡도를 가지기 때문에
# 아래 같이 일반적인 방법은 절대로 해결하지 못한다
# 이하 처음 시도했던 방식으로 시간초과 발생
"""
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    ch = list(map(int, stdin.readline().split()))
    result = 0
    for i in range(n - 1):
        ch.sort()
        mid = ch[0] + ch[1]
        result += mid
        ch.append(mid)
        ch.pop(0)
        ch.pop(0)
    print(result)
"""