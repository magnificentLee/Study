# 높거나 같을때 다음이 낮으면 초기화
# 낮거나 같을때 다음이 낮으면 초기화
# 를 어떻게 구현할까 고민하던차에 해당 문제가 dp인점을 이용
# 같을때 동시에 더해야 하기 때문에 if else(elif)문이 아닌 if if문으로
n = int(input())

array = list(map(int, input().split()))
dp_up = [1] * n
dp_down = [1] * n
for i in range(1, n):
    if array[i - 1] <= array[i]:
        dp_up[i] = max(dp_up[i], dp_up[i - 1] + 1)
    if array[i - 1] >= array[i]:
        dp_down[i] = max(dp_down[i], dp_down[i - 1] + 1)
print(max(max(dp_up), max(dp_down)))