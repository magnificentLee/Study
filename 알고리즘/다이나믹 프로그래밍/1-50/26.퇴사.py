# dp의 진행 방향은 블로그를 참고함
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    t, p = array[i]
    if i + t > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p + dp[i + t])
print(dp[0])