# [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 같은 방식으로 출력하기
# zip을 이용한 방법1
def solution(mylist):
    return list(map(list, zip(*mylist)))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# zip 없이 푼 방법1
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
# zip 없이 푼 방법2
"""
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
"""
# zip 없이 푼 방법3
"""
def solution(mylist):
    n = len(mylist)
    answer = [[mylist[row][column] for row in range(n)] for column in range(n)]
    return answer
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""