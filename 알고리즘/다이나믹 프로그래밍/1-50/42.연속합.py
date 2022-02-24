# 현재와 현재까지 더한 값들을 비교하여 현재 값을 최대로 갱신해준다
# 예를 들어 -4 10 인 경우 max(10, -4 + 10)
# -1 -4 10 인 경우 max(-4, -4 - 1) = -4 => -4 10 (10, 10 - 4) = 10

n = int(input())
array = list(map(int, input().split()))
for i in range(1, n):
    array[i] = max(array[i], array[i] + array[i - 1])
print(max(array))
