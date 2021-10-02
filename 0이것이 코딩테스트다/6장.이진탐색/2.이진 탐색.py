# 입력값
"""
10 7
1 3 5 7 9 11 13 15 17 19
10 7
1 3 5 6 9 11 13 15 17 19
"""
# 출력값
"""
4
원소가 존재하지 않습니다.
"""
# 반으로 쪼개면서 탐색하기
"""
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif array[mid] > target:  # 중간값이 목표보다 크면 끝을 줄여나가는 방식
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:  # 중간값이 목표보다 작으면 앞을 증가시키는 방식
        return binary_search(array, target, mid + 1, end)

# n, target = 10 7
n, target = list(map(int, input().split()))
# array = 1 3 5 7 9 11 13 15 17 19
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)  # 인덱스는 0부터 시작하기 때문
"""
# 반복문으로 구현하기
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
