# 1부터 10까지(인덱스 0~9) 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# 기본 리스트 dp = [1, 1, 1] 일 때
# 인덱스 3부터는 dp[i - 2] + dp[i - 3] 인 것 같음
# dp문제들을 꾸준히 풀어왔다면 알겠지만 이전의 문제들보다 규칙도 한 눈에 보이고 구현도 어렵지도 않은데
# 어째서 실버3인지 이해가 되지 않음
# 구현으로 따지면 훨씬 어려운데도 실버5인 문제도 수두룩한데 실버5 혹은 실버4가 어울리는 문제인것 같음
# 빠른 입력 결과 84ms -> 68ms로 단축됨
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [1, 1, 1]
    for i in range(3, n):
        tmp = dp[i - 2] + dp[i - 3]
        dp.append(tmp)
    print(dp[n - 1])