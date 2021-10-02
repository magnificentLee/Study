# 함수형태
from sys import stdin

input = stdin.readline


def box(n, m, array):
    result = 0
    # count = 0으로 할 경우 밑에 if문을 거칠때 상자를 다 채우지 못한 경우 4 / 6 인경우 0으로 출력될것
    count = 1
    if n == 0:
        count = 0
    while array:
        book = array.pop()
        result += book
        if result > m:
            count += 1
            result = book
    return count


n, m = map(int, input().split())
books = list(map(int, input().split()))
print(box(n, m, books))
"""
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())  # 박스의 개수, 박스에 넣을 수 있는 최대 무게

books = list(map(int, input().split()))
result = 0
count = 1
while books:
    book = books.pop()
    result += book
    if result > m:  # 박스를 초과하면
        count += 1
        result = book  # 다음 박스에 들어갈 무게
if n == 0:
    count = 0
print(count)
"""

