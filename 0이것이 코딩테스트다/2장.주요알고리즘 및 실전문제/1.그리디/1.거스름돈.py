# 500, 100, 50원으로 거슬러줌, 거스름돈은 10의 배수이다.
# 거슬러 줘야 할 동전의 최소 개수 구하라
"""
n = int(input())
coin = [500, 100, 50]
count = 0
for i in coin:
    count += n // i
    n %= i
print(count)
"""
# 각각의 동전 개수를 찾는 방법
n = int(input())
coin = [500, 100, 50, 10]
coin_list = []
for i in coin:
    coin_list.append(n // i)
    n %= i
for j in range(len(coin)):
    print("{}원 : {}".format(coin[j], coin_list[j]), end=" ")