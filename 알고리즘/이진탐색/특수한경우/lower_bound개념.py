# array = [3, 3, 4, 9, 2, 5, 3, 4]
# 해당 리스트가 2×10^5 개 까지 있다고 할 때 제한된 시간안에 각각의 값의 제일 앞의 인덱스를 뽑는 방법은?
# 이러한 문제에서 lower_bound 가 필요함
# lower_bound : 찾고자 하는 값의 가장 처음으로 나오는 위치를 찾는 함수
# 단순 이진탐색으로 풀 경우 처음, 중간, 끝 중에서 숫자만 맞으면 결과를 출력하기 때문에 오답이 발생
# end = mid 라는 방법을 이용해 숫자가 같고 start != end 일 때 end의 값을 쳐내는 방법을 이용하면 lower_bound를 구현할 수 있음

# 백준 20551 Sort 마스터 배지훈 문제를 예시로 들자
n, m = map(int, input().split())
arrayA = sorted([int(input()) for _ in range(n)])
arrayB = [int(input()) for _ in range(m)]

for i in range(m):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arrayA[mid] == arrayB[i]:
            if start == end:
                print(mid)
                break
            end = mid
        elif arrayA[mid] < arrayB[i]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(-1)
"""
input
8 4
3
3
4
9
2
5
3
4
3
10
4
2
output
1
-1
4
0
"""