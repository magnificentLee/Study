# 다른 사람 방식
n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    for j in range(0, i, 1):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])