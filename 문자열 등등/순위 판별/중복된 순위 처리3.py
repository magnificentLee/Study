# 기초적인 방법
# 석차 구하기
# input
# 5
# 90 85 92 95 90
# output
# 3 5 2 1 3
n = int(input())
score = list(map(int, input().split()))
for i in range(n):
    tmp = 1
    for j in range(n):
        if score[i] < score[j]:  # 낮은 값을 구하는 식
            tmp += 1
    print(tmp, end=" ")
# 리스트를 이용하는 방식
"""
result = []
for i in range(n):
    tmp = 1
    for j in range(n):
        if score[i] < score[j]:  # 낮은 값을 구하는 식
            tmp += 1
    result.append(tmp)
print(*tmp)
"""