# 최초풀이
"""
def solution(mylist):
    answer = [int(i) for i in mylist]
    return answer
print(solution(["1", "100", "33"]))
"""
def solution(mylist):
    answer = list(map(int, mylist))
    return answer
print(solution(["1", "100", "33"]))