# 백준 4158 CD
# 입력값으로 0, 0 이 들어오면 입력 종료임
# pypy3으로도 1468ms가 걸림
# 반복문을 입력외에는 사용하면 절대 안 될 것 같음
from sys import stdin
input = stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    array1 = [int(input()) for _ in range(n)]
    array2 = [int(input()) for _ in range(m)]
    # 인덱스로 진행
    result = 0
    for target in array2:
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if array1[mid] == target:
                result += 1
                break
            elif array1[mid] < target:
                start = mid + 1
            elif array1[mid] > target:
                end = mid - 1
    print(result)
