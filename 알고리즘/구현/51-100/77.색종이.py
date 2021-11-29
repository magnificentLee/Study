# 최종적으로 통과한 코드 (3중 for문 전부 제거, 결과를 list에 저장하는 방식 제거)
# 미리 행, 열의 최대 길이를 계산하여 최종 카운트때 그 범위내에서만 작동하게끔 바꿨음
# 서브태스크1~3 : 다른 사람의 코드보다 약 2배정도 빠름
array = [[0 for _ in range(1001)] for _ in range(1001)]  # 1001, 1001
row, col = 0, 0
for i in range(int(input())):
    a, b, x, y = map(int, input().split())
    tmp_row = a + x
    tmp_col = b + y
    if tmp_row > row:
        row = tmp_row
    if tmp_col > col:
        col = tmp_col
    idx = i + 1
    for j in range(b, b + y):
        array[j][a:(a + x)] = [idx] * x
size = max(row, col)
for i in range(1, idx + 1):
    result = 0
    for j in range(size):
        result += array[j].count(i)
    print(result)

# row, col 의 최댓값을 구해 넓이를 구할 때 array의 전체를 탐색하지 않아도 되게 수정했음
# 시간이 약 4배 정도 짧아졌지만 그래도 53점임, 채점 결과 서브태스크4에서 시간 초과가 발생함
# 반복적인 for문(특히 3중 for문) 으로 인해 시간복잡도가 올라간 것으로 보임
"""
array = [[0 for _ in range(1001)] for _ in range(1001)]  # 1001, 1001
row, col = 0, 0
for i in range(int(input())):
    a, b, x, y = map(int, input().split())
    tmp_row = a + x
    tmp_col = b + y
    if tmp_row > row:
        row = tmp_row
    if tmp_col > col:
        col = tmp_col
    idx = i + 1
    for j in range(a, a + x):
        for k in range(b, b + y):
            array[j][k] = idx
result = [0] * idx
for n in range(idx):
    for i in range(row):
        for j in range(col):
            if array[i][j] == n + 1:
                result[n] += 1
print(*result, sep="\n")
"""

# 아래는 처음 작성했던 코드, 시간 초과가 날 것을 예상하고 제출했음 (서브태스크 과제로 53점)
"""
array = [[0 for _ in range(1001)] for _ in range(1001)]  # 1001, 1001

for i in range(int(input())):
    a, b, x, y = map(int, input().split())
    idx = i + 1
    for j in range(a, a + x):
        for k in range(b, b + y):
            array[j][k] = idx
result = [0] * idx
for n in range(idx):
    for i in range(1001):
        for j in range(1001):
            if array[i][j] == n + 1:
                result[n] += 1
print(*result, sep="\n")
"""