import sys

t = int(input())  # 전체 길이
n_list = []
for i in range(t):
    n = int(sys.stdin.readline())
    n_list.append(n)
    le = 0  # le = length
    if n == 0:  # 최근 숫자가 0이면
        le = len(n_list)  # 리스트 길이를 측정, 최근 숫자들을 없애기 위함
        del n_list[le - 2: le]  # if 1 2 3 4 5 6 0 -> 1 2 3 4 5
print(sum(n_list))
