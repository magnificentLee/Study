my_str = input().strip()
my_str_list = sorted(set(my_str))
num_list = [my_str.count(i) for i in my_str_list]
idx = [i for i, j in enumerate(num_list) if j == max(num_list)]
print(*[my_str_list[i] for i in idx], sep="")