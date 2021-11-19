# 피보나치
# idx: 0 1 2 3 4 5 6 7 ..  10
# num: 0 1 1 2 3 5 8 13 .. 55
n = int(input())
dp = [0] * 5000  # n = 4999 까지 가능, 더 높은 값을 원하면 5000보다 크게 하면 됨
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
