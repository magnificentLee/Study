# 참고로 빠른입력을 사용해도 시간이 828ms임 안 쓰면 아마도 시간초과날듯?
from sys import stdin

input = stdin.readline

n = int(input())

l = sorted([int(input()) for _ in range(n)], reverse=True)
# 가장큰 변 < 나머지의 합 이 중요한점
# 어차피 내림차순이므로 l[i](가장큼) > l[i + 1] > l[i + 2] 순서일것임
# if n == 3 이면 한 번만 하면 됨
flag = 0
for i in range(n - 2):
    if l[i] < l[i + 1] + l[i + 2]:
        print(l[i] + l[i + 1] + l[i + 2])
        flag = 1
        break
if flag == 0:
    print(-1)