# 백준 2417 정수 제곱근
# 정수 제곱근을 출력하는 문제
# 예를 들어 144는 12, 121은 11 이런식
# 일반적인 제곱근을 구하는 풀이 (부동소수점 오차가 존재함)는 오답이니 이진탐색으로 풀것
# 일반적인 풀이로 풀 경우 예를들어 9223372030926249000 의 경우 3037000499가 아닌 3037000500이 나옴
# 아래는 일반적인 정수 제곱근 풀이
"""
n = int(input())
result = int((n - 1) ** 0.5 ) + 1
print(result)
"""
# 이진탐색으로 제곱근을 구할 수 있다는 건 처음 알았음
from sys import stdin
input = stdin.readline

n = int(input())
start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1
print(start)
