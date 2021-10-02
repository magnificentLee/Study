n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
repair = []
for i in range(n - 7):  # 체스판을 8*8로 자른경우1, 경우2 ...
    for j in range(m - 7):  # 체스판을 8*8로 자른경우1, 경우2 ...
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