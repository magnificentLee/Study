# 1, 2, 5, 7 최소가 되게끔
# 거스름돈 문제의 경우 보통 그리디로 풀 수 있지만 해당 문제는 그리디로 풀 수 없음, dp로 풀어야함
# dp로 최댓값 리스트를 (n + 1) 개만큼 만들어줌
# 인덱스를 맞춰주기 위해 dp[0] = 0으로 만들어줌
# 12 = 7, 5
# 17 = 7, 5, 5
n = int(input())
dp = [100001] * (n + 1)
dp[0] = 0
coins = [7, 5, 2, 1]
for m in range(1, n + 1):
    for c in coins:
        if c <= m and dp[m - c] + dp[c] < dp[m]:
            dp[m] = dp[m - c] + dp[c]
        elif c == m:
            dp[m] = 1
print(dp[n])