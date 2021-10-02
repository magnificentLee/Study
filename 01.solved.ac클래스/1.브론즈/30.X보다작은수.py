# 시도1 : 성공
"""
n, x = map(int, input().split())
n_list = list(map(int, input().split()))
a = [i for i in n_list if i < x]
for i in a:
    print(i, end=" ")
"""
# 옛날 방법
n, x = map(int, input().split())
n_list = list(map(int, input().split()))
for i in n_list:
    if i < x:
        print(i, end=" ")
