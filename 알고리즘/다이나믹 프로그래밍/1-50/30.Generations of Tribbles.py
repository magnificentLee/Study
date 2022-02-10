# 쿵 피보나치
# koong 피보나치라는 자체제작 피보나치임
# n < 2 : 1
# n = 2 : 2
# n = 3 : 4
# n > 3 : [n - 1] + [n - 2] + [n - 3] + [n - 4]
# n번째 피보나치 : 0 <= n <= 67
dp = [0] * 68
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
for _ in range(int(input())):
    n = int(input())
    if n > 3:
        for i in range(4, n + 1):
            if not dp[i]:
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
            else:
                continue
    print(dp[n])
