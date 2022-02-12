# 뭔가 간단할것 같으면서도 딱 떠오르지 않음
# dp와 array의 시작값을 맞춰서 dp[i], array[i] 에 인덱스 조정없이 바로 접근하려고 했으나
# 입력값이 n = 1, array = -5 일때 max값으로 0이 출력된다는 오류가 발견됨 => max(dp[1:])로 조정하여 해결
for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    array = [0] + list(map(int, input().split()))
    dp[1] = array[1]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + array[i], array[i])
    print(max(dp[1:]))
    print(dp)

"""
2
1
-5    : 마지막에 dp[1:]로 해준 이유
14 
0 3 -1 -7 2 9 -1 -1 -1 -1 -1 5 -2 3   : dp[i] = max(dp[i - 1] + array[i], array[i])로 해준 이유
"""