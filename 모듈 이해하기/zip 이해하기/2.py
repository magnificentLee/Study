def solution(mylist):
    return list(map(list, zip(*mylist)))  # map, list 가 없으면 리스트 안에 튜플 형태로 묶어줌
# 리스트의 전체 길이만큼 zip으로 묶어줌 전체 길이: 3 = 내부 요소의 개수: 3
n = [[1, 2], [3, 4], [5, 6]]  # [[1, 3, 5], [2, 4, 6]]
m = [[1, 2, 3], [4, 5, 6]]  # [[1, 4], [2, 5], [3, 6]]
print(solution(n), solution(m), sep="\n")