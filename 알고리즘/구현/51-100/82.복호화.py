# 1. 띄어쓰기(공백)의 처리
# 2. set 를 쓸 경우 바로 list화 할 수 없음('set' object is not subscriptable)
for _ in range(int(input())):
    n = input().replace(" ", "")
    n_list = [i for i in set(n)]
    n_count = []
    for i in n_list:
        n_count.append(n.count(i))
    if n_count.count(max(n_count)) > 1:
        print("?")
    else:
        print(n_list[n_count.index(max(n_count))])
