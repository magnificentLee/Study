# 도우만 써도 되고 토핑은 같은 종류만 2개 이상 선택 불가능 (중요, 같은것 중복만 안 됨)
# 1원당 열량의 최댓값을 구하는 문제
# 토핑을 내림차순으로 정렬한 다음
# 기본(도우), 토핑1(도우 + 토핑), 토핑2(도우 + 토핑 + 토핑) 까지만 비교하면 될 것임
# 소수점 이하는 버림
n = int(input())
a, b = map(int, input().split())  # 도우 가격, 토핑 가격
c = int(input())  # 도우 열량
topping = sorted([int(input()) for _ in range(n)], reverse=True)
result = c // a  # 도우만 있을 때
with_topping = (c + topping[0]) // (a + b)
iter = 1
while True:
    if result > with_topping:
        break
    result = with_topping
    iter += 1
    with_topping = (c + sum(topping[:iter])) // (a + (b * iter))
print(result)