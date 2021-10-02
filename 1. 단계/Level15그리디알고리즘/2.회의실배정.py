# 회의가 겹치지 않는 최대 수를 구하는 문제
# 이전 회의의 끝나는 시간을 기준으로
# 다음 회의의 시작 시간이 이전 회의의 끝나는 시간보다 크거나 같을 경우 카운트
# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
"""
from sys import stdin
n = int(stdin.readline())
time = []
for _ in range(n):
    start, end = map(int, stdin.readline().split())
    time.append([start, end])
# time = sorted(time, key=lambda x: x[0])
time.sort(key=lambda x: x[0])
# time = sorted(time, key=lambda x: x[1])
time.sort(key=lambda x: x[1])
last = 0
result = 0
for i, j in time:
    if i >= last:
        result += 1
        last = j
print(result)
"""
from sys import stdin
n = int(stdin.readline())
time = []
last = 0
result = 0
for _ in range(n):
    start, end = map(int, stdin.readline().split())
    time.append([start, end])
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
for i, j in time:
    if i >= last:
        result += 1
        last = j
print(result)