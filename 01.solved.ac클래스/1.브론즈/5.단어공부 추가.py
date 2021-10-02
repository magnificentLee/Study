# 방법1 가장 빠른방법(120ms)
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
"""
# 방법2 가장 느린방법(604ms)
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
# 방법3 가장 최근시도, 중간속도(484ms)
alpha = list(input().upper())
alpha_list = []
for i in set(alpha):
    alpha_list.append(alpha.count(i))
max_list = [i for i, j in enumerate(alpha_list) if j == max(alpha_list)]
if len(max_list) > 1:
    print("?")
else:
    print(list(set(alpha))[max_list[0]]) # 어차피 max_list 요소는 한 개