n, m = map(int, input().split())

price = sorted([int(input()) for _ in range(m)])
max_price = max_total = 0  # 개당 최대 가격, 총합 최대 가격
for i in range(m):
    i_total = min(m - i, n)  # 구매자의 전체 숫자는 계란의 숫자를 넘지 않게
    if max_total < price[i] * i_total:
        max_price = price[i]
        max_total = price[i] * i_total
print(max_price, max_total)