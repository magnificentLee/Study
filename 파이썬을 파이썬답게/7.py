# 최초풀이
"""
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        if i == len(mylist) - 1:
            break
        answer.append(abs(mylist[i] - mylist[i + 1]))
    return answer
numlist = [83, 48, 13, 4, 71, 11]
print(solution(numlist))
"""
def solution(mylist):
    result = [abs(mylist[i] - mylist[i + 1]) for i in range(len(mylist) - 1)]
    return result
print(solution([83, 48, 13, 4, 71, 11]))