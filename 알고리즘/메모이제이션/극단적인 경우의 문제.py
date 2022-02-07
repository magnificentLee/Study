# 백준 1904 01타일 문제
# 시간제한 0.75초, 입력값의 범위는 1~1백만
# 문제에 주어진 15746으로 나누는 과정을 거치지 않으면 무조건 시간 초과가 걸림
# 예를 들어 입력값이 1백만이면 최소 1분 이상이 걸릴 것임
# 문제의 규칙을 직접 계산해본 결과 피보나치 수열임 - dp 폴더의 27번 참고

# 정답1, 468ms
"""
import sys

n = int(sys.stdin.readline())
dp = [1, 2]
for i in range(2, n + 1):
    tmp = (dp[i - 2] + dp[i - 1]) % 15746
    dp.append(tmp)
print(dp[n - 1])
"""
# 빠른 입력이 없으면 436ms 가 걸림
# tmp 식을 append에 바로 넣으니  408ms까지 줄어들었음
n = int(input())
dp = [1, 2]
for i in range(2, n + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % 15746)
print(dp[n - 1])
# 이외에도 [0] * (n + 2) 의 dp 리스트를 만들어
# 값을 저장하는 방법도 있음
