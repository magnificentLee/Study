# 백준 9291 스도쿠 채점
# 스도쿠 판별 방법
# 정수 1~9가 각 행, 각 열, 3 * 3 정사각형에 정확히 한 번씩 등장해야함
# 각 테스트 케이스는 9개의 줄로 구성
# 3 * 3 행렬을 체크 하는 점에서 조금 헤맸고
# 각 행, 열을 체크할 때 리스트를 초기화 한다는 것을 깜빡해서 틀렸던 문제
# 실버4인 이유는 3 * 3 체크 구현 때문에 그런것 같음
# 생각보다 시간이 널널한 편이라 3중 반복문까지 돌려도 괜찮았음
from sys import stdin
input = stdin.readline

t = int(input())
for n in range(t):
    array = [list(map(int, input().split())) for _ in range(9)]
    result = True
    for i in range(9):
        check_row = []  # 행 체크용
        check_col = []  # 열 체크용
        for j in range(9):
            check_row.append(array[i][j])
            check_col.append(array[j][i])
        if len(set(check_row)) != 9 or len(set(check_col)) != 9:
            result = False
            break
    if result:  # 위 반복문에서 INCORRECT인 경우 시간 절약용
        for k in range(3):
            check_list = []
            x = k * 3
            y = k * 3
            for i in range(3):
                for j in range(3):
                    check_list.append(array[i + x][j + y])
            if len(set(check_list)) != 9:
                result = False
                break
    print("Case %i: " % (n + 1), end="")
    if result:
        print("CORRECT")
    else:
        print("INCORRECT")
    if n != (t - 1):
        blank = input()