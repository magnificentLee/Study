# 힙에 튜플을 원소로 추가하거나 삭제하면 튜플 내에서 맨 앞에 있는 값을 기준으로
# 최소 힙이 구성되는 원리를 이용
import heapq
nums = [4, 1, 7, 3, 8, 5]
heap = []
for num in nums:
    heapq.heappush(heap, (-num, num))

while heap:
    print(heapq.heappop(heap)[1])