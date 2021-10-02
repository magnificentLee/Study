# 튜플의 두 번째 원소 즉, 나이를 기준으로 내림차순 정렬하는 경우
result = sorted([("홍길동", 35), ("이순신", 75), ("아무개", 50)], key = lambda  x: x[1], reverse=True)
# x = 소괄호, y, z, 아무렇게나 써도 상관 X

print(result)
