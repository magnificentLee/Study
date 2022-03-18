# 백준 2776 암기왕
# 시간초과
# 원인을 파악하지 못해 많이 틀렸음
# 결과를 보고 납득한게 반복문을 이용해 재귀적으로 풀었는데 7436ms가 걸림
# 검색을 통해 알게된 부분
# 1. 메모리
# 재귀함수는 함수를 반복적으로 호출하기 때문에 스택 메모리를 사용함(스택 오버플로우가 발생할 수 있음)
# 반복문은 메모리 힙을 사용함

# 2. 코드길이
# 재귀함수는 반복문에 비해 길이를 단축할 수 있음

# 중요한 점
# 재귀함수는 반복문에 비해 시간, 메모리가 더 소요됨
# 그럼에도 재귀함수를 사용하는 이유는 가독성이 좋고 변수 사용을 줄여주기 때문임

# 결론
# 해당 문제는 dp를 이용한 반복문과 일반적인 재귀함수를 비교하면 이해가 편할 것임
# 피보나치 문제에서 두 가지 해결법중 dp를 이용한 반복문(혹은 치환을 이용한 반복문)이 압도적으로 빠르지만
# 재귀함수를 이용하면 매우 느림, 최대 재귀 깊이도 정해져있음

# 이진탐색(재귀함수가 아닌 반복문을 이용한) 풀이, 아래보다 오래걸림
# 186608KB, 7436ms, 551B
from sys import stdin
input = stdin.readline


def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:  # array[mid] > target
            end = mid - 1
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    array = sorted(map(int, input().split()))  # 값을 크기 순서로 확인하기 때문에 정렬은 필수
    m = int(input())
    data = list(map(int, input().split()))
    for i in data:  # 이진탐색은 data값을 array에서 탐색하기 때문에 end 값은 n - 1임
        result = binary(i, 0, n - 1)
        print(result)


# 집합을 이용한 다른 방법(stdout을 추가해줬음)
# 214724KB, 1264ms, 303B
"""
from sys import stdin, stdout
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = set(map(int, input().split()))
    m = int(input())
    data = list(map(int, input().split()))
    for i in data:
        stdout.write("1\n") if i in array else stdout.write("0\n")  # stdout은 int형 출력불가, 개행포함X
"""
