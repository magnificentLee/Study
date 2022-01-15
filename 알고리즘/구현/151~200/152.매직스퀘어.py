# 수가 중복되는 경우를 생각하지 못해서 틀렸던 문제

from sys import stdin

n = int(stdin.readline().rstrip())
array = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
target = (n * (n ** 2 + 1)) // 2
flag = True
diag1, diag2 = 0, 0  # 좌우 대각선 확인용
count = 0  # 중복 확인용 카운트
for i in range(n):
    # 새로운 중복 확인용 구문, 2중 반복문마다 작동하지 않아도 되기 때문에 훨씬 빨라짐
    # 메모리는 4kb 증가한 대신 속도는 92->68ms
    if len(set(array[i])) != len(array[i]):
        flag = False
        break
    tmp = 0
    for j in range(n):
        tmp += array[j][i]  # 열 확인용
        # if array[j].count(array[j][i]) > 1:  기존 중복 확인용 구문
        #     count = 1
        #     break
    diag1 += array[i][i]
    diag2 += array[i][-(i + 1)]
    if target != sum(array[i]) or target != tmp or count > 0:  # sum : 행 확인용
        flag = False
        break
if not flag or target != diag1 or target != diag2:
    print("FALSE")
else:
    print("TRUE")