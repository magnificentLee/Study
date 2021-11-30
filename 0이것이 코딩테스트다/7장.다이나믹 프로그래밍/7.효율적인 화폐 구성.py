n, m = map(int, input().split())  # 화폐 갯수, 목표
array = [int(input()) for _ in range(n)]  # 각 화폐들의 가치

dp = [10001] * (m + 1)  # dp[0] 을 고려
dp[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # if문은 이해를 돕기위한 코드임, min 부분에서 항상 d[j] 값을 반환하기 때문에 없어도 상관은 없음
        if dp[j - array[i]] != 10001:  # i-k 원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - array[i]] + 1)
if dp[m] == 10001:  # 만들 수 없으면
    print(-1)
else:
    print(dp[m])