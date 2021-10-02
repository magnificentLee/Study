# 계속해서 최소값을 불러와주는 작업을 거쳐야 하는 경우 우선순위 큐 자료구조를 사용하면됨
# 파이썬에서 우선순위 큐(priorityQueue) = heapq 모듈
# 이하 예제 문제
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
        # heapq.heappush(추가대상리스트, 추가하려는 요소)
    while len(queue) > 1:
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        result += a + b
        heapq.heappush(queue, a + b)
    print(result)

# heappush() 함수는 O(logN)의 시간 복잡도를 가진다
# heappop() 함수도 O(logN)의 시간 복잡도를 가진다
# 두번째로 작은 원소를 얻으려면 heap[1] X
# heappop을 통해 가장 작은 원소를 삭제후 heap[0]을 통해 새로운 최솟값에 접근해야 함
# 기존 리스트를 힙으로 변환
"""
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)
# 결과 : [1, 3, 5, 4, 8, 7]
"""
"""
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] 방식으로 추가, 삭제되며
     1  ---> root
   /   \
  3     5
 / \   /
4   8 7
위 구조처럼 구성된다
"""