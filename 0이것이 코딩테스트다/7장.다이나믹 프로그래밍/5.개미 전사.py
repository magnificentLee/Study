n = int(input())

array = list(map(int, input().split()))
# 1 3 1 5
dp = [0] * 100
dp[0] = array[0]
dp[1] = max(array[0], array[1])
# dp = 1 , 3
for i in range(2, n):
    # max(3, 1 + array[3]: 1)
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])
    # max(3, 3 + array[4]: 5)
print(dp[n - 1])  # n = len of array(dp) 따라서 dp의 마지막 인덱스는 n - 1
