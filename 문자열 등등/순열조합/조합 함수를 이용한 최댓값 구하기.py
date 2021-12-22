# 백준 2303 숫자 게임
# 번호가 아래로 갈수록 커지기 때문에 값이 같거나 클 때 인덱스 값을 저장하게 했음
# 번호가 같거나 이기 때문에 최댓값이 같으면 더 큰 번호의 인덱스를 저장할 것
from itertools import combinations
from sys import stdin
input = stdin.readline

max_tmp = 0
for i in range(int(input())):
    a = map(int, input().split())
    array = list(combinations(a, 3))
    for j in array:
        tmp = (sum(map(int, j))) % 10
        if max_tmp <= tmp:
            max_tmp = tmp
            idx = i + 1
print(idx)