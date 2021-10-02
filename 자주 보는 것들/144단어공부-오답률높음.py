# Mississipi -> ?
# zZa -> Z
n = input().upper()
n_list = []
for i in set(n):
    n_list.append(n.count(i))
idx = [i for i, x in enumerate(n_list) if x == max(n_list)]
if len(idx) > 1:
    print("?")
else:
    print(list(set(n))[n_list.index(max(n_list))])
