# 이동 횟수가 4번 이하: 중복된 방법 혹은 위2칸오른쪽1칸, 아래2칸오른쪽1칸을 반복해도 됨
# 이 방식으로 그림을 그려보면 n > 2, m > 7 일 때 m - 2 라는 답이 나옴
from sys import stdin

def knight(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m + 1) // 2)
    else:
        if m < 7:
            return min(4, m)
        else:
            return m - 2


n, m = map(int, stdin.readline().split())
print(knight(n, m))
