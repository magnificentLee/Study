""" 1. 간략화한 방법
def make_list(string):
    return list(string)
print(make_list("abcd"))
"""
# for문을 이용한 방법
def make_list(string):
    my_list = []
    for i in string:
        my_list.append(i)
    return my_list

print(make_list("abcd"))