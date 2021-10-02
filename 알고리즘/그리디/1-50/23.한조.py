# 용들은 처음 출발한 봉우리보다 높은 봉우리를 만나면
# 그대로 공격을 포기하고 금강산자락에 드러누워 낮잠을 청한다고 한다.
# 조건확인
# 자신보다 낮은 값만 처리
# 중간에 시작보다 높은 값 만날 경우 종료
# 각각의 값들이 처리가능한 오른쪽 값의 최대 숫자를 구하라는 말
from sys import stdin
n = int(stdin.readline())
height = list(map(int, stdin.readline().split()))
max_height = 0
count = 0
result = 0
for i in height:
    if i > max_height:
        max_height = i
        count = 0
    else:
        count += 1
    result = max(result, count)
print(result)


# 첫 시도 : 문제 이해 잘못함
"""
from sys import stdin

n = int(stdin.readline())
e = list(map(int, stdin.readline().split()))
result = 0
for i in e[1:]:
    if i <= e[0]:
        result += 1
print(result)
# 반례
# 5
# 5 4 6 3 7  : 1이 정답이지만 2가 나옴
"""
# 시도2 : 시간초과 발생
"""
from sys import stdin
n = int(stdin.readline())
archer = list(map(int, stdin.readline().split()))
max_result = 0
for i in range(n):
    result = 0
    for j in archer[i + 1:]:
        if archer[i] > j:
            result += 1
        else:
            break
    if result > max_result:
        max_result = result
print(max_result)
"""