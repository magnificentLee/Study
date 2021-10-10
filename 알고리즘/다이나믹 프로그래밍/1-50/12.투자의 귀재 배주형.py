# dp의 기본은 문제를 나누어 푸는것
# 예를 들어 문제를 a, b 로 나누면 a를 이용해 b를 풀 수 있어야 한다
# 피보나치 수열에서 dp 리스트를 이용해 푸는것을 예로 들 수 있음
# 마지막 출력때 int 처리해도 46549가 아닌 46550이 나옴
# 각 dp를 계산해줄때 int 처리해야될듯 -> 맞음
h, y = map(int, input().split())
dp = [0] * (y + 1)
dp[0] = h
for i in range(1, y + 1):
    dp[i] = int(dp[i - 1] * 1.05)
    if i >= 3:
        dp[i] = max(int(dp[i - 3] * 1.2), dp[i])
    if i >= 5:
        dp[i] = max(int(dp[i - 5] * 1.35), dp[i])
print(dp[-1])
# 실패한 방법
"""
h, y = map(int, input().split())

interest = [(1, 0.05), (3, 0.2), (5, 0.35)]
interest_list = []
for i, j in interest:
    result = h
    tmp = y // i
    if tmp > 0:
        for _ in range(tmp):
            result += result * j
        interest_list.append(int(result))
print(interest_list)
"""