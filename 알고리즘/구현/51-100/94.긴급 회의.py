# 계수형태로 풀면 될듯
n = int(input())
array = [0] * n
players = list(map(int, input().split()))
for i in range(n):
    idx = players[i] - 1
    if idx < 0:
        continue
    else:
        array[idx] += 1
if array.count(max(array)) > 1:
    print("skipped")
else:
    print(array.index(max(array)) + 1)