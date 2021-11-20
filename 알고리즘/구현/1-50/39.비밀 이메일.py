#  전체 글자수 N, R행 C열
#  R<=C이고, R*C=N인 R과 C를 고른다.
#  만약, 그러한 경우가 여러 개일 경우, R이 큰 값을 선택한다
string = list(input())
n = len(string)
r_c = [()]  # row & column 행 열
for i in range(1, n + 1):
    r = i
    c = n // i
    if r <= c and r * c == n:
        r_c.append((r, c))  # 행, 열
row = r_c[-1][0]
col = r_c[-1][1]
# 실제 구성은 행 열이지만 리스트에 추가되는 방식은 동일 열의 다른 행에 추가되는 방식이므로
# 반복문 구성때는 비틀어서 진행
result = [["" for _ in range(col)] for _ in range(row)]  # r * c 행렬 생성
idx = 0
for i in range(col):
    for j in range(row):
        result[j][i] = string[idx]
        idx += 1
# 이하 정상적인 행렬 진행
for i in range(row):
    for j in range(col):
        print(result[i][j], end="")