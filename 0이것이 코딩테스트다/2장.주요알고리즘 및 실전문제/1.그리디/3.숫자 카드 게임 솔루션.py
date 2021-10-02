# min() 함수를 이용하는 방법

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)  # 이전 값과 새로 들어온 값을 비교해서 최댓값 출력

print(result)