# 최대 글자갯수 15개
dp = [[0] * 15 for _ in range(5)]
for i in range(5):
    string = list(input())
    for j in range(len(string)):
        dp[i][j] = string[j]
for i in range(15):
    for j in range(5):
        if dp[j][i] == 0:
            continue
        print(dp[j][i], end="")