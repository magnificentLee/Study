# 백준 5426 비밀 편지 문제
# 정사각형 크기의 행렬에 넣어서 열 : 역순, 행 : 그대로 출력
for _ in range(int(input())):
    n = input()
    l = len(n)
    row = int(l ** 0.5)  # row, col
    array = ["" for _ in range(row)]
    idx = 0
    for i in range(row):
        array[i] += n[idx: row + idx]
        idx += row
    for i in range(row - 1, -1, -1):
        for j in range(row):
            print(array[j][i], end="")
    print()