# 마지막 날 보유한 코인을 모두 처분한다는 조건에 유의할 것
# 낮을 때 사서 높을 때 판다, 단 보유량이 0 일 땐 못 판다는점에 주의
from sys import stdin
n, w = map(int, stdin.readline().split())
coin = [int(input()) for _ in range(n)]
coin_count = 0

for i in range(n - 1):
    if coin_count == 0 and coin[i] < coin[i + 1]:
        coin_count += w // coin[i]
        w -= coin_count * coin[i]
    elif coin_count != 0 and coin[i] > coin[i + 1]:
        w += coin[i] * coin_count
        coin_count = 0
print(w + coin_count * coin[-1])