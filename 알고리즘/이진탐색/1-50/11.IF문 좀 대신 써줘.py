# 백준 19637 IF문 좀 대신 써줘
"""
if power <= 10000
 print WEAK
else if power <= 100000
 print NORMAL
else if power <= 1000000
 print STRONG
"""
# 이진탐색을 사용하는 게 중점
# 기본적인 구현 (시간초과가 발생할 것, 간략한 구조만 확인. 검색해보니 이진탐색만으로도 시간초과가 발생한다고함)
"""
n, m = map(int, input().split())
condition = []
for _ in range(n):
    a, b = input().split()
    condition.append((a, int(b)))
flag = [0] * m
array = [int(input()) for _ in range(m)]
for i in range(m):
    if not flag[i]:
        for j in range(n):
            if array[i] <= condition[j][1]:
                print(condition[j][0])
                break
"""
# 조건(condition 내용물)이 엄청 많은 경우를 생각하면 될듯
from sys import stdin
input = stdin.readline

def binary(arr, target):
    start, end = 0, len(arr) - 1
    index = 0
    while start <= end:
        mid = (start + end) // 2
        if target <= arr[mid][1]:
            end = mid - 1
            index = mid
        else:
            start = mid + 1
    return index


n, m = map(int, input().split())
condition = []
for _ in range(n):
    a, b = input().split()
    condition.append((a, int(b)))
for _ in range(m):
    power = int(input())
    idx = binary(condition, power)
    print(condition[idx][0])