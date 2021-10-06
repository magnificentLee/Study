# 아이디어를 새로 짰음
# 내림차순으로 정렬하여 값 + 인덱스를 하여 이 중 최솟값을 구하는 것
# 단, 4 5 6 7 8 같은 경우 뒤집고 더하면 8 8 8 8 8 로 최솟값이 8이 나온다
# 이런 경우를 대비하여 min(n, min(result))를 해준다
from sys import stdin
input = stdin.readline

n = int(input())
blocks = sorted(map(int, input().split()), reverse=True)
result = []
for i, j in enumerate(blocks):
    result.append(i + j)
print(min(n, min(result)))


# 모든 반례는 통과되지만 오답처리됨
# print(min(n, result)) 로 해봤지만 오답출력, 근본적으로 잘못 접근한 것일 수 있음
"""
from sys import stdin
input = stdin.readline

n = int(input())
blocks = sorted(map(int, input().split()))
blocks_max = max(blocks)
result = 0
stack = 0
for i in range(n - 1, -1, -1):
    le = len(blocks)
    blocks[i] -= stack
    if blocks[i] <= 0:
        continue
    if blocks[i] > blocks[le//2] or blocks[i] >= le:
        result += 1
        blocks.pop()
    else:
        stack += blocks[le//2]
        blocks[i] -= blocks[le//2]
        result += stack
print(min(n, result))
"""

