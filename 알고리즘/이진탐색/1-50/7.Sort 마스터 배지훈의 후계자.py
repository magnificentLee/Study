# 백준 20551 Sort 마스터 배지훈의 후계자
# n, 오름차순, m, 결과
# 9 -1  -1   0
# 0  0  10  -1
# -1 2   5  -1
# 3  3   9   4
# 2  9   0   1
# 리스트A에 중복으로 들어오는 경우에서 문제가 발생함
# 중복 문제인줄 알았지만 정확히는 중복된 값이 들어올 경우 가장 앞의 인덱스가 답임
# mid값으로 하면 그 사이 아무값을 출력하기 때문에 오답이 발생한것
# 찾아보니 lower_bound 라는 개념을 알아야 됨
# lower_bound : 찾고자 하는 값의 가장 처음으로 나오는 위치를 찾는 함수
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arrayA = sorted([int(input()) for _ in range(n)])
arrayB = [int(input()) for _ in range(m)]
for i in range(m):
    start, end = 0, n - 1  # 중복된 값의 경우 인덱스 초과 발생
    while start <= end:
        mid = (start + end) // 2
        if arrayA[mid] == arrayB[i]:
            if start == end:  # lower_bound 부분, 시작과 끝이 같아질 때 까지 끝부분을 계속 날려줌, 시작 = 끝이면 출력
                print(mid)
                break
            end = mid
        elif arrayA[mid] < arrayB[i]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(-1)