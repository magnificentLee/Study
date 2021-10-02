def solution(mylist):
    answer = list(map(len, mylist))
    return answer


print(solution([[1], [2]]))  # [1, 1]
print(solution([[1, 2], [3, 4], [5]]))  # 	[2, 2, 1
