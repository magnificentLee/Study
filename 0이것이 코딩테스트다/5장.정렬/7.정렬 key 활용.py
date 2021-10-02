# 방법1
"""
t = int(input())

dic = [input().split() for i in range(t)]
dic.sort(key=lambda x: x[1])
for i in range(len(dic)):
    print(dic[i][0], end=" ")
"""
# 방법2
"""
array = [("바나나", 2), ("사과", 5), ("당근", 3)]

array.sort(key=lambda x: x[1])
print(array)
"""
# 방법3
"""
array = [("바나나", 2), ("사과", 5), ("당근", 3)]
result = sorted(array, key=lambda x:x[1])
print(result)
"""
# 방법4 교재
array = [("바나나", 2), ("사과", 5), ("당근", 3)]

def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)