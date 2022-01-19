# 백준 2960
# n, k 가 주어질 때 k 번째 지워진 수를 출력
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())  # 전체N, K번째 지워진 수

flag = [0] * (n + 1)
count = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if not flag[j]:  # 방문하지 않았다면
            flag[j] = 1  # 방문처리
            count += 1  # 지워진 수 카운트
            if count == k:
                print(j)
                exit()