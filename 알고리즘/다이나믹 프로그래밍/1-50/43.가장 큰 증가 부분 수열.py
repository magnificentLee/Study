# 첫 코드 : 특정 반례에서(아마도) 막히는 코드
# 찾은 반례
# 3
# 20 10 15  : 정답 : 25, 현재 코드 : 20
"""
n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
dp[0] = array[0]
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])
print(max(dp))
"""
n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
dp[0] = array[0]
for i in range(1, n):
    dp[i] = array[i]  # 20 10 인 경우 if문에 들어가지 않기 때문에 10이 아닌 0이 나옴
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])
print(max(dp))

""" else문 추가시
5
1 7 4 3 5 에서 1 4 5 = 10 이 아닌 9가 나옴(오답)
else문이 아닌 처음부터 넣으면 되지 않을까? => 정답
"""