"""
def solution(mylist):
    answer = [[] for _ in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i].append(mylist[j][i])
    return answer

a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution(a_list))
"""
# 솔루션 1
"""
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
"""
# 솔루션 2
"""
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
"""
# 솔루션 3
# mylist의 길이는 mylist[0]의 길이와 같다는 조건에서 가능
def solution(mylist):
    n = len(mylist)
    answer = [[mylist[row][column] for row in range(n)] for column in range(n)]
    return answer
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))