# 규칙을 파악해보자
# i = 1 : 1 = 1
# i = 2 : 1+1 2 = 2
# i = 3 : 1+1+1 1+2 2+1 3 = 4
# i = 4 : 1+1+1+1 1+1+2 1+2+1 2+1+1 1+3 3+1 2+2 = 7
# i = 5 : 1+1+1+1+1 1+1+1+2 1+1+2+1 1+2+1+1 2+1+1+1 1+2+2 2+1+2 2+2+1 1+1+3 1+3+1 3+1+1 2+3 3+2 = 13
# ...
# i=1,2,3 일 때의 경우와 i >= 4 일 때의 경우로 나누자
# 7 = 1 + 2 + 4   : i[4] = i[1] + i[2] + i[3]
# 13 = 2 + 4 + 7  : i[5] = i[2] + i[3] + i[4]

# 첫 제출, 30864KB 72ms 366B
"""
from sys import stdin
input = stdin.readline

t = int(input())
array = [0] * 11
array[1] = 1
array[2] = 2
array[3] = 4
for _ in range(t):
    n = int(input())
    if array[n] == 0:  # 중복 계산 제거용
        for i in range(n + 1):
            if i < 4:
                continue
            else:
                array[i] = array[i - 1] + array[i - 2] + array[i - 3]
    print(array[n])
"""

# 두 번째 제출, 30864KB 68ms 336B
from sys import stdin
input = stdin.readline

t = int(input())
array = [0] * 11
array[1] = 1
array[2] = 2
array[3] = 4


def check(n):
    for i in range(4, n + 1):
        array[i] = array[i - 1] + array[i - 2] + array[i - 3]
    return


for _ in range(t):
    n = int(input())
    if array[n] == 0:  # 중복 계산 제거용
        check(n)
    print(array[n])

# 세 번째 제출, 30864KB 72ms 227B
"""
from sys import stdin
input = stdin.readline

t = int(input())
array = [0, 1, 2, 4]
for i in range(4, 11):
    array.append(array[i - 1] + array[i - 2] + array[i - 3])
for _ in range(t):
    n = int(input())
    print(array[n])

"""