# nCm = (n! / m! * (n - m)!)
# 단순한 조합 구현 문제, math 라이브러리의 factorial 함수를 이용해도 되고 단순히 반복문을 사용해도 되고
# 각각의 경우를 구하는 문제는 아니기 때문에 itertools의 combinations를 이용하는건 아닌것 같음

n, m = map(int, input().split())
upper, lower1, lower2 = 1, 1, 1
# n! 부분
for i in range(n, 0, -1):
    upper *= i
# m! 부분
for i in range(m, 0, -1):
    lower1 *= i
# (n - m)! 부분
for i in range(n - m, 0, -1):
    lower2 *= i
print(upper // (lower1 * lower2))

# 왜 dp문제인지 이해가 안 가서 블로그들을 찾아봤는데 대부분은 위의 반복문 혹은 factorial을 이용했고
# 아래는 dp를 이용했던 블로그
"""
import sys
n , m = map(int, sys.stdin.readline().split(" "))
dp = [[0 for i in range(101)] for j in range(101)]
for i in range(1,101):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2,101):
    for t in range(1,i):
        dp[i][t] = dp[i-1][t-1] + dp[i-1][t]
print(dp[n][m])
"""