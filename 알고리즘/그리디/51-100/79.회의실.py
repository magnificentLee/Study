# 각 회의 시간이 겹치면 안 됨
# 시작 시간, 끝나는 시간 순으로 정렬, 앞 번의 끝나는 시간과 뒷 번의 시작 시간을 비교해서 카운트하면 될 것
from sys import stdin
input = stdin.readline

n = int(input())
room = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
room.sort(key=lambda x: x[1])
time = 0
result = 0
for i, j in room:
    if i >= time:
        result += 1
        time = j
print(result)

