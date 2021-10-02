"""
a = input().split("-")
a_list = []
for i in a:
    a_list.append(i[0])
for i in a_list:
    print(i, end="")
"""
# 더 간단하게
a = input().split("-")
for i in a:
    print(i[0], end="")