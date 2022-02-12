# 백준 14495 피보나치 비스무리한 수열
# 단순 피보나치, 시간제한, 메모리 모두 널널함 절대 실버3 문제는 아님 (실버5~4 정도가 적당한듯)
n = int(input())
dp = [0, 1, 1, 1]
for i in range(4, n + 1):
    dp.append(dp[i - 3] + dp[i - 1])
print(dp[n])