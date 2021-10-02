# 시도1 : 성공 but 시간을 너무 오래 잡아먹음
"""
a = sorted(input().upper())
a_up_list = list(set(a))
count_list = []
for i in a_up_list:
    count_list.append(a.count(i))
if count_list.count(max(count_list)) > 1:
    print("?")
else:
    idx = count_list.index(max(count_list))
    print(a_up_list[idx])
"""
n = input().upper()
n_list = []
for i in set(n):
    n_list.append(n.count(i))
idx = [i for i, x in enumerate(n_list) if x == max(n_list)]
if len(idx) > 1:
    print("?")
else:
    print(list(set(n))[n_list.index(max(n_list))])