price = int(input())
count = 0
coins = [500, 100, 50, 10]
for coin in coins:
    count += price // coin
    price %= coin
print(count)