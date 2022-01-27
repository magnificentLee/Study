# 메모이제이션을 이용한 피보나치수열
# 기존 방법(단순 함수, 반복문)으로는 1000 이상의 피보나치를 구하는건 많은 시간이 걸렸음
# 메모이제이션을 이용하면 이전 계산값을 저장하여 참조하기 때문에 시간을 획기적으로 줄일 수 있음
# 참고로 치환하는 방법을 이용하면 시간을 절반가까이 더 줄일 수 있음!
import time
start = time.time()
# 피보나치 시작
n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
# 피보나치  끝
end = time.time()
print(end - start)