"""
import sys
t1 = int(sys.stdin.readline())
n1 = list(map(int, sys.stdin.readline().split()))
t2 = int(sys.stdin.readline())
n2 = list(map(int, sys.stdin.readline().split()))
for i in n2:
    if i in n1:
        print(1)
    else:
        print(0)
# 의문점
# n 과 m 의 범위가 상당히 넓은데 시간초과가 걸리지 않을까
"""
# 684ms 526B
import sys
t1 = int(sys.stdin.readline())
n1 = sorted(map(int, sys.stdin.readline().split()))
t2 = int(sys.stdin.readline())
n2 = map(int, sys.stdin.readline().split())

def binary(arr, val, start, end):  # start, end
    # start에 들어가는 mid 값이 계속 커지거나 end 값이 계속 작아지는 경우
    #  즉, 값을 찾지 못하는 경우
    if start > end:
        return 0  # False
    mid = (start + end) // 2
    if arr[mid] > val:  # val(구하려는값) = 3, mid = 5 일 때 mid를 빼줘서 3으로 갈 수 있게
        return binary(arr, val, start, mid - 1)
    elif arr[mid] < val:  # mid를 더해줘서 val에 가까워지게
        return binary(arr, val, mid + 1, end)
    else:  # arr[mid] == val, 즉, val 값을 찾았을 때 = 참
        return 1  # True

for i in n2:
    start = 0
    end = len(n1) - 1
    print(binary(n1, i, start, end))

"""
# 148ms 206B
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write("1\n") if l in N else stdout.write("0\n")
"""