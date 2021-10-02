# 예제(설명)를 다시 읽어보자
# idx : 1 2 3 4 5
# val : 3 1 4 3 2
# idx 순서로 더할시 39
# val 순서로 더할시 32
# 즉, 값이 클수록 뒤로 가야 중간 값에 영향을 덜 끼친다
# 따라서 val 순서로 정렬을 해주면 될 것이다.
n = int(input())
val = sorted(map(int, input().split()))
time = 0
result = 0
for i in val:
    time += i
    result += time
print(result)
# 빠른 입출력
"""
from sys import stdin
n = int(stdin.readline())
val = sorted(map(int, stdin.readline().split()))
time = 0
result = 0
for i in val:
    time += i
    result += time
print(result)
"""