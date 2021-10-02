# 점화식 : dp[i] = dp[i - 1] + dp[i - 2]
t = int(input())
# 피보나치 : 1 1 2 3 / 5 8...
# 0 혹은 1이 나오는 순간 : idx 3까지
dp = [(1, 0), (0, 1), (1, 1), (1, 2)] + [(0, 0) for _ in range(37)]

for _ in range(t):
    n = int(input())
    for i in range(4, n + 1):  # dp식에서 0~3 까진 이미 정해놨기 때문에
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])
    print(*dp[n])
