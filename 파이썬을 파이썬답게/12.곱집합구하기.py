"""
list1 = "ABCD"
list2 = "xy"
list3 = "1234"
for i in list1:
    for j in list2:
        for k in list3:
            print(i, j, k)
"""
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
#print(list(itertools.product(iterable1, iterable2, iterable3)))
# 요소를 붙이고 싶으면 join을 사용
num = list(itertools.product(iterable1, iterable2, iterable3))
result = ["".join(i) for i in num]
print(*result, sep="\n")