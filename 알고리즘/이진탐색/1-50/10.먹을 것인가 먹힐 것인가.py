# 백준 7795 먹을 것인가 먹힐 것인가
# 기본적인 구현방법은 쉬운데 조건을 맞추는게 까다로울듯
# n, m 은 최대 2만까지 가능하므로 2중 반복문이면 20000 * 20000 까지도 나올듯
# 따라서 가장 기초적인 for for를 이용한 풀이는 아닐것임
# 무작위 값이 들어오는 리스트이기 때문에 최악의 경우를 생각하여 팀정렬을 이용한다고 생각하면
# 리스트의 전체를 확인 할 필요는 없을 것임
# 해당 코드로는 408ms 즉, 단순 리스트 비교는 무조건 시간초과임!!
from sys import stdin
input = stdin.readline

def binary(arr, target):
    start, end = 0, len(arr) - 1
    idx = -1
    while start <= end:
        mid = (start + end) // 2
        if target > arr[mid]:
            idx = mid
            start = mid + 1
        else:
            end = mid - 1
    return idx


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    array_a = sorted(map(int, input().split()))
    array_b = sorted(map(int, input().split()))
    result = 0
    for i in array_a:
        result += (binary(array_b, i) + 1)  # 인덱스라 +1을 해줘야 정답임
    print(result)