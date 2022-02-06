# 1부터 10까지(인덱스 0~9) 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# 기본 리스트 dp = [1, 1, 1] 일 때
# 인덱스 3부터는 dp[i - 2] + dp[i - 3] 인 것 같음
# 피보나치 예제와 다른 점은 미리 데이터 리스트를 데이터 전체 크기만큼 만들지 않는 것
# dp[i]에 직접 접근해 데이터를 더하거나 추가하는 것과 달리 append를 이용해 추가함
# append의 시간 복잡도는 1이기 때문에 이것도 좋은 방법인 것 같음
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [1, 1, 1]
    for i in range(3, n):
        tmp = dp[i - 2] + dp[i - 3]
        dp.append(tmp)
    print(dp[n - 1])