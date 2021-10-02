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
n = input().upper()
n_list = []
for i in set(n):
    n_list.append(n.count(i))
idx = [i for i, x in enumerate(n_list) if x == max(n_list)]
if len(idx) > 1:
    print("?")
else:
    print(list(set(n))[n_list.index(max(n_list))])
""" if input = zZa
input().upper() = "ZZA"
list(set(n)) = "A", "Z"
n_list = 1, 2
n_list.index() = n_list의 인덱스 값 찾기 : 1 = 0, 2 = 1 
max(n_list) = 2
따라서 n_list.index(2) = 1
list(set(n))[1] = "Z"
"""