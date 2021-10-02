# 최초풀이
"""
def solution(mylist):
    result = []
    for i in mylist:
        result += i
    return result
print(solution([[1], [2]]))
"""
mylist = [[1, 2], [3, 4], [5, 6]]
# 방법1. sum
"""
result = sum(mylist, [])
print(result)
"""
# 방법2. itertools.chain
"""
import itertools
print(list(itertools.chain.from_iterable(mylist)))
"""
# 방법3. itertools, unpacking
"""
import itertools
print(list(itertools.chain(*mylist)))
"""
# 방법4. list comprehension 이용
"""
result = [i for array in mylist for i in array]
print(result)
"""
# 방법5, 6. reduce 함수 이용
from functools import reduce
result1 = list(reduce(lambda x, y: x + y, mylist))
print(result1)
import operator
result2 = list(reduce(operator.add, mylist))
print(result2)