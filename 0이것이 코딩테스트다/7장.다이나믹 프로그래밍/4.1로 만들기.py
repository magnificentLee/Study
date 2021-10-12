n = int(input())
dp = [0] * 30001
# dp[0] = 0
# dp[1] = 0  : 목표값이 1이기 때문
for i in range(2, n + 1):
    # 아래 방식은 1씩 계속해서 늘어날것임 : 0 0 1 2 3 4...
    # 하지만 3의 경우 1, 4의 경우 2, 5의 경우 1, 6의 경우 2, 7은 3 같은 방식이여야함
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[n])