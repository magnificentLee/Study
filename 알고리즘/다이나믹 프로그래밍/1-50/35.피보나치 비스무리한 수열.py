# 단순 피보나치, 시간제한, 메모리 모두 널널함 왜 실버3인지 모르겠음
n = int(input())
dp = [0, 1, 1, 1]
for i in range(4, n + 1):
    dp.append(dp[i - 3] + dp[i - 1])
print(dp[n])