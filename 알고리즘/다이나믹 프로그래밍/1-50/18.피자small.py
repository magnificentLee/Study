# 백준 14606
# 연계 문제로 입력값이 매우 큰 14607 피자 (Large)가 있음
# 아래 dp코드 외에도 최적화된 식이 있음 : n * (n - 1) // 2
n = int(input())
dp = [0] * 11
dp[1] = 0
dp[2] = 1
for i in range(3, n + 1):
    m = i // 2
    dp[i] = (i - m) * m + dp[i - m] + dp[m]
print(dp[n])