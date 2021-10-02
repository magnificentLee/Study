import math

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0

    num = math.floor(math.sqrt(distance))
    n_square = num ** 2
    n_increase = math.sqrt(n_square)

    if distance > n_square + n_increase:
        count = 2 * num + 1
    elif n_square < distance <= n_square + n_increase:
        count = 2 * num
    elif distance == n_square:
        count = 2 * num - 1

    if distance < 4:
        count = distance

    print(count)
