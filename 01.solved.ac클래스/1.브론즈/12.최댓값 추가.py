# 1
"""
n = [int(input()) for i in range(9)]
n_list = [[i, j] for i, j in enumerate(n) if j == max(n)]
print(n_list[0][1], n_list[0][0] + 1, sep="\n")
"""
n = [int(input()) for _ in range(9)]
print(max(n), n.index(max(n)) + 1, sep="\n")