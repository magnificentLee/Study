n = int(input())
dp = [0] * 11
dp[1] = 0
dp[2] = 1
for i in range(3, n + 1):
    m = i // 2
    dp[i] = (i - m) * m + dp[i - m] + dp[m]
print(dp[n])