# k명에게 나눠줄 수 있는 최대 용량을 구하는 문제
# start를 0으로 잡으면 zerodivisionError가 발생함
# k명에게 나눠줄 수 있는 최대 용량을 구하는 문제
# start를 0으로 잡으면 zerodivisionError가 발생함
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
array = sorted([int(input()) for _ in range(n)])
start, end = 1, array[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(n):
        tmp += array[i] // mid
    if tmp >= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)