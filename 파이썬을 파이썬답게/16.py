def solution(mylist):
    result = [i ** 2 for i in mylist if i % 2 == 0]
    return result
print(solution([3, 2, 6, 7]))