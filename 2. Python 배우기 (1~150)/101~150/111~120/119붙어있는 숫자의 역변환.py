n_list = list(map(int, input()))
n_list.sort(reverse=True)
for n in n_list:
    print(n, end="")
