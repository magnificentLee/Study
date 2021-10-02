# 시도1 : 성공 but 공간복잡도 높음
"""
n_list = []
for i in range(9):
    n_list.append(int(input()))
idx = [[i, x] for i, x in enumerate(n_list)]
print(max(n_list), idx[n_list.index(max(n_list))][0] + 1, sep="\n")
"""
# 시도2
n_list = []
for i in range(9):
    n_list.append(int(input()))
print(max(n_list), n_list.index(max(n_list)) + 1, sep="\n")
