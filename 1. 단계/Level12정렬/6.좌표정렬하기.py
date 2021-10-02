# sort 의 정렬 방법을 알아둘 필요가 있다
# sort 는 첫 번째 요소가 같으면 자동으로 두 번째 요소를 비교해서 정렬해준다
# sort 대신 lambda 함수를 이용하는 방법도 있음
# 방법1 424ms 192B 48892KB
"""
import sys

t = int(sys.stdin.readline())
num = []
for _ in range(t):
    num.append(list(map(int, sys.stdin.readline().split())))
num.sort()
for i in range(t):
    print(num[i][0], num[i][1])
"""
# 방법2 432ms 203B 56660KB
import sys

t = int(sys.stdin.readline())
num = []
for _ in range(t):
    num.append(list(map(int, sys.stdin.readline().split())))
num.sort(key=lambda x: (x[0], x[1]))
for i in num:
    print(i[0], i[1])