t = int(input())
n_list = []
for i in range(t):
    x, y = map(int, input().split())
    n_list.append([x, y])
for i in n_list:
    rank = 1
    for j in n_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")