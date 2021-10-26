# 입력값 설명이 많아서 그렇지 천천히 읽어보면
# 전체 라운드 수
# A의 입력값 개수, 입력값 크기들
# B의 입력값 개수, 입력값 크기들
# 1 4 : 전체 개수1, 내용물 = 4
# 4 3 3 2 1 : 전체 개수4, 내용물 = 3, 3, 2, 1

# counter 함수
# 입력값이 많은 순서로 값을 정리함
# 입력값
# 4 3 4 2 2 1 1 1
# 출력값
# Counter({'1': 3, '4': 2, '2': 2, '3': 1})
# 입력의 첫번째는 전체 리스트의 길이이므로 무시
from collections import Counter as ct

t = int(input())
for _ in range(t):
    a = ct(input().split()[1:])
    b = ct(input().split()[1:])
    for i in "4321":
        if a[i] != b[i]:
            print("A" if a[i] > b[i] else "B")
            break
    else:
        print("D")
