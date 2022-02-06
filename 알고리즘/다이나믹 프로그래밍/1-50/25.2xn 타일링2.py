# 이번엔 2*1, 1*2, 2*2 세 가지 방식으로 채울 수 있음
# n = 1 2 3 4
#cnt= 1 3 5 11
# 규칙을 보니 i = 3 부터, dp[n-2]*2 + dp[n-1] 인 것 같음
# 또 문제 조건에서 10007을 빼는 것을 깜빡해서 틀림, 주의할 것
import sys
n = int(sys.stdin.readline())
dp = [1, 3]
for i in range(2, n):
    tmp = dp[i - 2] * 2 + dp[i - 1]
    dp.append(tmp)
print(dp[n - 1] % 10007)
