"""
import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
length = []
first = 1
for _ in range(k):
    lan.append(int(sys.stdin.readline()))
while True:
    result = 0
    for i in lan:
        result += i // first
    if result == n:
        length.append(first)
    if result < n:
        print(max(length))
        break
    first += 1
"""
# 결과
# length 리스트 :
# [186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
# 예상되는 문제
# 1.리스트 추가로 인한 메모리초과
# 2.입력값의 범위로 인한 시간초과
# 실제 결과
# 2번 시간초과 발생
# 시간초과 방지를 위해 이진탐색(이분탐색)을 해야되지 않을까
import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)  # 랜선 길이의 최솟값, 최댓값
result = 0
while start <= end:  # if start > end; break
    # 몇 cm의 크기로 자를 것인가
    mid = (start + end) // 2
    lines = 0
    # 해당 크기로 자르면 몇 개의 랜선이 모이는가
    for i in lan:
        lines += i // mid
    # 잘라낸 개수가 기준보다 많다면, 더 큰 단위로 잘라서 개수를 줄여야 한다.
    if lines >= n:
        result = mid
        start = mid + 1
    # 잘라낸 개수가 기준보다 적다면, 더 작은 단위로 잘라서 개수를 늘려야 한다.
    else:
        end = mid - 1
print(result)
# result를 없애고 print(end)로 해도 됨
# end가 이진탐색의 종료값이기 때문