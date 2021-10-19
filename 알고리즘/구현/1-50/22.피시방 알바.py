# 처음 시도했던 방식 : 실패
"""
n = int(input())

dp = [0] * 101

dudes = list(map(int, input().split()))

for i in dudes:
    dp[i] = 1
print(dp.count(0) - 1)
"""
# 정도로 가는게 정답이었다
n = int(input())

dp = [0] * 101

dudes = list(map(int, input().split()))
result = 0
for i in dudes:
    if dp[i] == 0:
        dp[i] = 1
    else:
        result += 1
print(result)