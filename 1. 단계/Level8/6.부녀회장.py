t = int(input())
for _ in range(t):
    floor = int(input())
    room = int(input())
    floor_zero = [i for i in range(1, room + 1)]
    for j in range(floor):
        for k in range(1, room):
            floor_zero[k] += floor_zero[k - 1]
    print(floor_zero[-1])
