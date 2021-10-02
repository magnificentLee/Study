from sys import stdin
import heapq
n = int(stdin.readline())
card = [int(stdin.readline()) for _ in range(n)]
q = []
result = 0
for i in card:
    heapq.heappush(q, i)
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a + b
    heapq.heappush(q, a + b)
print(result)