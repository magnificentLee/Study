import sys

n_list = []
for i in range(9):
    n_list.append(int(sys.stdin.readline()))
n_list.sort()
result = sum(n_list)
for i in range(9):
    for j in range(i + 1, 9):
        if result - n_list[i] - n_list[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(n_list[k])
            exit()