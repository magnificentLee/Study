# dp : 각각의 array[0][0] 의 값만큼 아래 혹은 오른쪽으로 이동할 때
# 오른쪽 : array[j][값]에서 array[n - 1][n - 1]에 도착할 수 있다면 dp[j][값] = dp[0][0] + 1
# 아래 : array[값][i]에서 array[n - 1][n - 1]에 도착할 수 있다면 dp[값][i] = dp[0][0] + 1
# 아니라면 해당 위치에서 오른쪽 혹은 아래로 이동
from sys import stdin
input = stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1  # 시작 포함
for j in range(n):
    for i in range(n):
        if j == n - 1 and i == n - 1:
            print(dp[j][i])
            break
        pos = array[j][i]
        ny = j + pos
        nx = i + pos
        if nx < n:  # x축 이동(오른쪽)
            dp[j][nx] += dp[j][i]
        if ny < n:  # y축 이동(아래)
            dp[ny][i] += dp[j][i]

"""
반례
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
출력
1
0
0
0
        if array[j][i] == array[n - 1][n - 1]:
            print(dp[j][i])
            break
해당 종료 조건이 문제임
값으로 비교하기 때문에 틀리는것
인덱스가 동일한지로 바꾸자
"""