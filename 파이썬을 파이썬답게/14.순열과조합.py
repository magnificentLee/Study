# 최초풀이
"""
from itertools import permutations

def solution(mylist):
    mylist.sort()
    answer = list(map(list, permutations(mylist, len(mylist))))
    return answer
print(solution([3, 1, 2]))
"""
from itertools import permutations

def solution(mylist):
    answer = sorted(map(list, permutations(mylist, len(mylist))))
    return answer
print(solution([3, 1, 2]))
