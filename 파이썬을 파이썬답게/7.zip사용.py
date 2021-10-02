def solution(mylist):
    answer = []
    for i, j in zip(mylist, mylist[1:]):
        answer.append(abs(i - j))
    return answer, list(zip(mylist, mylist[1:]))  # lsit;zip = 확인용
print(solution([83, 48, 13, 4, 71, 11]))
# 결과 : [35, 35, 9, 67, 60]
# [(83, 48), (48, 13), (13, 4), (4, 71), (71, 11)]
# 즉, zip 함수에서 서로 길이가 다른 리스트가 인자로 들어오는 경우
# 길이가 짧은 쪽 까지만 조합이 이루어짐
