# 각 숫자를 문자로 지정, 9를 카운트 한 리스트로 대체
# 1 2 3 9     0 0 0 1
# 4 5 9 6  => 0 0 1 0
# 9 7 8 9     1 0 0 1
# 각 행, 열 별로 합친 값 = 최대치, 전체 9 리스트의 합 - 최대치 = 정답일듯
n, m = map(int, input().split())
array = [input().split() for _ in range(n)]
total = 0
# 리스트를 카운트 리스트로 변환 및 전체 구하기
for i in range(n):
    for j in range(m):
        array[i][j] = str(array[i][j].count("9"))
        total += int(array[i][j])
row, col = 0, 0
# 행에서 최댓값 찾기
for i in range(n):
    tmp = 0
    for j in range(m):
        tmp += int(array[i][j])
    if tmp > row:
        row = tmp
# 열에서 최댓값 찾기
for i in range(m):
    tmp = 0
    for j in range(n):
        tmp += int(array[j][i])
    if tmp > col:
        col = tmp
print(total - max(row, col))
# 1번 풀이의 문제를 못 찾고 수정했던 코드, 제출후 1번 코드 오류 확인후 통과함
# 2번 풀이가 384 / 404ms 로 더 빠름
"""
n, m = map(int, input().split())
array = [input().split() for _ in range(n)]
total = 0
# 리스트를 카운트 리스트로 변환 및 전체 구하기
for i in range(n):
    for j in range(m):
        array[i][j] = str(array[i][j].count("9"))
        total += int(array[i][j])
row, col = [], []
# 행에서 최댓값 찾기
for i in range(n):
    tmp = 0
    for j in range(m):
        tmp += int(array[i][j])
    row.append(tmp)
# 열에서 최댓값 찾기
for i in range(m):
    tmp = 0
    for j in range(n):
        tmp += int(array[j][i])
    col.append(tmp)
print(total - max(max(row), max(col)))
"""