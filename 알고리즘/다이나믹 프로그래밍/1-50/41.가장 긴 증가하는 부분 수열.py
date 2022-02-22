# 6
# 10 20 10 30 20 50
# 여기서 가장 긴 증가하는 수열은
# 10 20 X  30 X  50
# 이중 for문을 사용하면 될듯?

# 다음은 파이썬용 풀이
n = int(input())
array = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):  # i까지의 수열을 확인
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# 아래는 다른 언어를 고려한 풀이
"""
n = int(input())  # len of array
array = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if array[j] < array[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
"""