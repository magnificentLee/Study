# 최초풀이
def solution(mylist):
    answer = ""
    for i in mylist:
        answer += i
    return answer
print(solution(["1", "100", "33"]))
"""
def solution(mylist):
    answer = "".join(mylist)
    return answer
print(solution(["1", "100", "33"]))
"""