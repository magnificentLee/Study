# 아이디어
# 최저 비용을 구하기 위해선 기름 값이 가장 낮을 때 전부 사면 될 것임(도착지점을 제외한 가격)
# 만약 가장 낮은 가격이 아니라면 다음 도시만큼 기름을 사들이면 됨
"""
from sys import stdin

n = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
gs = list(map(int, stdin.readline().split()))
first = gs[0]
result = 0
for i in range(len(road)):
    if gs[i] <= first:
        first = gs[i]
    result += first * road[i]
print(result)
"""
from sys import stdin

n = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
gas = list(map(int, stdin.readline().split()))
minval = gas[0]
result = 0
for i in range(len(road)):  # gas의 마지막값(도착지)는 필요 없기 때문에
    if gas[i] <= minval:
        minval = gas[i]
    result += gas[i] * road[i]  # gas[i]로 할 경우 5 6(다음 값이 더 큰 경우)인 경우 큰 값에 사버림
print(result)