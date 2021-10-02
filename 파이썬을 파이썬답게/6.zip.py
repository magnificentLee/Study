"""
def solution(mylist):
    return list(map(list, zip(*mylist)))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
number = [1, 2, 3, 4]
name = ["lee", "kim", "sin", "hong"]
# result = list(zip(number, name))
# 결과 : [(1, 'lee'), (2, 'kim'), (3, 'sin'), (4, 'hong')]
result = list(map(list, zip(number, name)))
# 결과 : [[1, 'lee'], [2, 'kim'], [3, 'sin'], [4, 'hong']]
print(result)