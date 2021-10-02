from sys import stdin
n = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
city = list(map(int, stdin.readline().split()))
minval = city[0]
result = 0
for i in range(len(road)):
    if city[i] <= minval:
        minval = city[i]
    result += minval * road[i] # city[i]로 할 경우 5 6(다음 값이 더 큰 경우)인 경우 큰 값에 사버림
print(result)