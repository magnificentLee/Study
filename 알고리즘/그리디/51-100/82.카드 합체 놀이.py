# 힙큐를 이용한 방식 : 결과는 두 배 이상 빠름
# 힙큐 : 이진 트리 기반의 자료구조
# heap 생성 : 빈 리스트 생성 ([])
# item 을 heap 에 삽입 : heapq.heappush(heap, item)
# heap 의 마지막 요소 삭제 : heapq.heappop(heap)
from sys import stdin
import heapq
input = stdin.readline

n, m = map(int, input().split())
initial_cards = list(map(int, input().split()))
cards = []
for i in initial_cards:
    heapq.heappush(cards, i)
for i in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    plus = card1 + card2
    heapq.heappush(cards, plus)
    heapq.heappush(cards, plus)
print(sum(cards))
# 기본적인 방식
"""
n, m = map(int, input().split())

cards = list(map(int, input().split()))
result = 0
for i in range(m):
    cards.sort()
    result = cards[0] + cards[1]
    cards[0] = result
    cards[1] = result
print(sum(cards))
"""