# 예시로 나온 방법을 참고하자
# 12345 의 경우 총 4가지 : 1-2345,12-345,123-45,1234-5 로 나타낼 수 있음
# 즉, 길이만큼 반복
# 각 값을 str로 리스트화, 반복문으로 조합하여 비교해보자
# 짧게 줄인 방식
n = list(input())
flag = 0
for i in range(1, len(n)):
    start = 1
    end = 1
    for j in n[:i]:
        start *= int(j)
    for j in n[i:]:
        end *= int(j)
    if start == end:
        print("YES")
        break
else:
    print("NO")
# 처음 방식
"""
n = list(input())
flag = 0
for i in range(1, len(n)):
    start = 1
    end = 1
    for j in n[:i]:
        start *= int(j)
    for j in n[i:]:
        end *= int(j)
    if start == end:
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")
"""