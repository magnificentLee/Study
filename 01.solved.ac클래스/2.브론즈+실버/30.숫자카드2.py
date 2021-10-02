"""
import sys

t1 = int(sys.stdin.readline())
n1 = sorted(map(int, sys.stdin.readline().split()))
t2 = int(sys.stdin.readline())
n2 = list(map(int, sys.stdin.readline().split()))

def binarysearch(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            return binarysearch(arr, val, mid + 1, end)
        elif arr[mid] > val:
            return binarysearch(arr, val, start, end - 1)
        else:
            return arr.count(val)
    return 0
start = 0
end = len(n2) - 1
for i in n2:
    print(binarysearch(n1, i, start, end), end=" ")
"""
# 6 3 2 10 10 10 -10 -10 7 3
# 10 9 -5 2 3 4 5 -10

# 런타임에러 발생
# 파이썬에서 재귀함수는 오류 방지를 위해 깊이 제한을 해뒀는데
# 기본 최대 깊이는 1000임
import sys
from collections import Counter


t1 = int(sys.stdin.readline())
n1 = sorted(map(int, sys.stdin.readline().split()))
t2 = int(sys.stdin.readline())
n2 = list(map(int, sys.stdin.readline().split()))
result = []
count = Counter(n1)
for i in n2:
    print(count[i], end=" ")
