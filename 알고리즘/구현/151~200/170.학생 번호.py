# 학생들의 번호 길이는 같음
# 시간 단축을 위해 빠른 입력을 사용 : 108ms -> 72ms로 단축
from sys import stdin
input = stdin.readline

n = int(input())
array = [input().rstrip() for _ in range(n)]
l = len(array[0])
count = 1  # 마지막(혹은 시작) 포함
for i in range(l - 1, -1, -1):
    array_set = set()
    for j in range(n):
        array_set.add(array[j][i:])
    if len(array_set) == n:
        break
    else:
        count += 1
print(count)