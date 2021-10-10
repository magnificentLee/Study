# 런타임에러 발생
# n = 0 일때 문제가 발생하는것
# dp[0] * (n + 1)이 아닌 dp[0] * 10001을 해줄것
n = int(input())

dp = [0] * 10001
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])