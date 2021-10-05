# 반례 6 1 2 3 4 5 7 8 인 경우를 고려한 아이디어
# 시작값보다 큰 경우 max 값을 바꿔준다
# 추가로 시작값보다 큰 경우, 시작값보다 1만큼 큰 경우(연속된 경우) interlinked 값을 늘려준다
# 마지막으로 리스트 전체 길이 - interlinked(이어진 값)을 구해주면 옮겨야 될 값이 나온다
from sys import stdin

input = stdin.readline

n = int(input())

books = [int(input()) for _ in range(n)]
interlinked = 1  # 블레이드러너를 보고 생각난 변수
books_max = books[0]
for i in range(1, n):
    if books[i] > books_max:
        if books[i] == books_max + 1:
            interlinked += 1
        books_max = books[i]
print(len(books) - interlinked)
# 처음 시도한 아이디어
# 최댓값과 연속된 수 제외, 처음 값이 max인 경우 제외
# 예를 들어 1 5 3 4 2 = 4 와 1 4 5 3 2 = 3
# 3 1 = 1 혹은 1 = 0
# 하지만 처음 값이 max는 아니지만 연결되는 경우 오답 처리됨
# 예를 들어 6 1 2 3 4 5 7 8 처럼 1 2 3 4 5 를 빼면 6 7 8 이 연결되서 8 - 3 = 5 가 답이지만 6으로 나옴
"""
from sys import stdin

input = stdin.readline

n = int(input())

books = [int(input()) for _ in range(n)]
max_books = max(books)
iter = books.index(max(books))
count = 1
for i in range(n):
    if iter == 0:
        count = 1
        break
    else:
        if books[iter - (i + 1)] == max_books - 1:
            count += 1
        if iter - (i + 1) == 0:
            break
        if
print(len(books) - count)

"""