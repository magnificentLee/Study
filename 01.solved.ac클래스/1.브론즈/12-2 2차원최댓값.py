# 2566번
n_list = []
max_num = []
for i in range(9):
    n_list.append(list(map(int, input().split())))
for i in n_list:
    max_num.append(max(i))
column = max_num.index(max(max_num))  # 가로 좌우(행)
row = n_list[column].index(max(max_num))  # 세로 위아래(열)
print(max(max_num))
print(column + 1, row + 1)