# 1층 1 3 6
# 0층 1 2 3
# 따라서 1층 3호는 6명
t = int(input())
for _ in range(t):
    floor, room = int(input()), int(input())
    floor_zero = [i for i in range(1, room + 1)]
    for j in range(floor):
        for k in range(1, room):
            floor_zero[k] += floor_zero[k - 1]
    print(floor_zero[-1])
