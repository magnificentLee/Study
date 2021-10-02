# 방법1
"""
white = [["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"]]
black = [["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"],
         ["B", "W", "B", "W", "B", "W", "B", "W"],
         ["W", "B", "W", "B", "W", "B", "W", "B"]]
n, m = map(int, input().split())  # if 8 8 : 세로, 가로
board = []
result = []
for _ in range(n):  # 8줄 입력
    board.append(list(input()))
for i in range(m - 7):  # i :0~1
    q = 0  # 열
    w = 0  # 행 (좌우)
    for j in range(n - 7):  # j : 0~1
        count_black = 0
        count_white = 0
        for k in range(i, i + 8):  # k : 0~8 , 1~9
            for l in range(j, j + 8):  # l : 0~8, 1~9
                if board[l][k] != white[q][w]:
                    count_white += 1
                if board[l][k] != black[q][w]:
                    count_black += 1
                w += 1
            w = 0
            q += 1
        q = 0
        result.append(count_black)
        result.append(count_white)
print(min(result))
"""
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
repair = []

for i in range(n - 7):  # 최대 크기 조절용 8 * 8
    for j in range(m - 7):  # 최대 크기 조절용 8 * 8
        first_white = 0
        first_black = 0
        for k in range(i, i + 8):  # 각 위치들의 인덱스값 ex) White(0,0), Black(0, 1), ...
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != "W":
                        first_white += 1
                    if board[k][l] != "B":
                        first_black += 1
                else:
                    if board[k][l] != "B":
                        first_white += 1
                    if board[k][l] != "W":
                        first_black += 1
        repair.append(first_white)
        repair.append(first_black)
print(min(repair))