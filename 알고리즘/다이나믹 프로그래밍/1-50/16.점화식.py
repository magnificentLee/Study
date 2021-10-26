# 변형 피보나치로 생각되며 재귀, 메모이제이션을 사용하면 될듯
"""
i = 1
dp[1] = dp[0] * dp[0]
dp[2] = dp[0] * dp[1] + dp[1] * dp[0]
dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
dp[i] =

"""
n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])