"""
idx: 1 2 3 4 5 6 7 8 9

num: 1 2 2 3 3 3 4 4 4 4

따라서 (3, 7) = 2 + 3 + 3 + 3 + 4 = 15
"""
a, b = map(int, input().split())

num_list = []
for i in range(1, 46):
    num_list += [i] * i
print(sum(num_list[a - 1:b]))
