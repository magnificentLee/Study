# 범위가 정해져있다는 점에 주목, 계수정렬을 사용하면 어떨까
# 계수정렬을 이용한 풀이
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    array = [0] * 1001
    for i in range(n):
        array[int(input())] += 1
    print(array.index(max(array)))

# 집합을 사용하면 리스트를 이미 정렬했더라도 무작위로 정렬된 집합을 만들기 때문에 해당 문제에 맞지 않을것임
# 값의 범위가 1~1000 이라는 점에 주목, 중복된 값을 만나면 다음 반복문을 진행하게 하여 시간을 줄일 수 있을 것임
"""
for _ in range(int(input())):  # 전체 테스트 케이스
    n = int(input())
    array = sorted([int(input()) for _ in range(n)])
    result, count = 0, 0
    for i in array:
        if result == i:  # 이미 카운트 했던 값이라면
            continue
        tmp = array.count(i)
        if count < tmp:
            count = tmp
            result = i
    print(result)
"""