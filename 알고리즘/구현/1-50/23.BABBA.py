# A  0  : 0 0
# B  1  : 0 1
# BA 1  : 1 1
# BAB  2 : 1 2
# BABBA 3 : 2 3
# A : dp[n - 1], B : dp[n]
# 이전 방식은 함수로 푸는 방식, 이게 더 간결함
dp = [0] * 46
dp[1] = 1
n = int(input())
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n - 1], dp[n])