# 최댓값을 구하는 문제임에도 그리디가 아닌 다이나믹 프로그래밍인 이유가 뭘까
# 전체 갯수와 점수의 범위가 넓기 때문?
# 예제의 경우로 생각해보자
# 10 20 15 25 10 20
# idx=3일때 경우: 10+20+0+25=55, 10+0+15+25=50
# idx=5일때 경우: 0+20+15+0+10+20=65, 10+20+0+25+20=75
# 각각의 경우는 dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i]
# dp아 array의 범위를 n만큼 지정해줬기 때문에 n = 1일 때 인덱스에러가 발생하는것 같음
# 문제에 제시된 300만큼의 범위로 지정하자
# 빠른 입력을 사용한 결과 런타임에러(인덱스에러)가 발생

n = int(input())
array = [0] * 301
for i in range(n):
    array[i] = int(input())
dp = [0] * 301
dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[0] + array[2], array[1] + array[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + array[i - 1] + array[i], dp[i - 2] + array[i])
print(dp[n - 1])