# 푸는데 좀 많이 걸림
# 특히 규칙 파악하는데 오래 걸렸음
# 상근 시작, 상근(SK) 창영(CY) / N개의 돌, 1턴에 1, 3, 4개 중 선택해서 가져갈 수 있음
# 완벽하게 게임을 하며 마지막 돌을 가져가는 사람이 이김 (각자 최적의 경우로 시행함)
# 6 : SK : 4, 1, 1 = sk cy sk
n = int(input())
dp = [0, 1, 0, 1, 1]
for i in range(5, n + 1):
    if dp[i - 4] and dp[i - 3] and dp[i - 1]:
        dp.append(0)
    else:
        dp.append(1)
print("SK" if dp[n] else "CY")