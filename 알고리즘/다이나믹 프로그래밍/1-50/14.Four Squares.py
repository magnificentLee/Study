# 예외 사항들 때문에 다른 방법이 필요
"""
import math
n = int(input())
sqrt_n = int(math.sqrt(n))
sqrt_list = [i ** 2 for i in range(sqrt_n + 1)]
l = len(sqrt_list)
dp = []
for i in range(1, l):
    result = sum(sqrt_list[i:])
    if result == n:
        dp.append((l - i, result))
print(min(dp[0]))
# 예외 상황 : 26: 답x, 34567: 인덱스 에러
"""
# 시간초과가 발생하는 방법
"""
# 각 값의 제곱근까지만 확인하면 됨
import math

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    # i의 제곱 = 1 ex) dp[1], dp[4], dp[9]... = 1
    dp[i] = 1 if int(math.sqrt(i)) ** 2 == i else i
for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
print(dp[n])
"""
# 각 값의 제곱근까지만 확인하면 됨
# python 3 으로 도저히 해결이 안 됐기 때문에 pypy로 제출함

n = int(input())
dp = [0, 1]
for i in range(2, n + 1):
    min_val = 1e9
    j = 1
    while (j ** 2) <= i:
        min_val = min(min_val, dp[i - (j ** 2)])
        j += 1
    dp.append(min_val + 1)

print(dp[n])
