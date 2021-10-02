from collections import Counter

grounds = []
for i in range(3):
    grounds.extend(list(map(int, input().split())))
    gg = Counter(grounds)
    print(gg.keys())
    print(gg.items())
"""
input : 0 0 0 0
dict_keys([0])
dict_items([(0, 4)])
input : 0 0 0 0
dict_keys([0])
dict_items([(0, 8)])
input : 0 0 0 1
dict_keys([0, 1])
dict_items([(0, 11), (1, 1)])
Process finished with exit code 0
"""