from sys import stdin
input = stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
start, end = 0, max(array)
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in array:
        result += min(mid, i)
    if result <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)