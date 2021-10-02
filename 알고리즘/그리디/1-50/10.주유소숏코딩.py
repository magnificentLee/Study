n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
r = price[0]
result = road[0] * r

for i in range(1, n - 1):
    r = min(r, price[i])
    result += r * road[i]
print(result)