# 1차 : 결과 정상
"""
t, price = map(int, input().split())
coin = sorted([int(input()) for _ in range(t)], reverse=True)
result = 0
for i in coin:
    if price >= i:
        result += price // i
        price %= i
print(result)
"""
# 2차
t, price = map(int, input().split())
coin = sorted([int(input()) for _ in range(t)], reverse=True)
result = 0
for i in coin:
    result += price // i
    price %= i
print(result)