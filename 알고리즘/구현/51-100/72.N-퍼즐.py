"""
.BCD ABCD 1000
EAGH EFGH 0100
IJFL IJKL 0010
MNOK MNO. 0001
"""
# 맨해튼 거리 = 각 좌표의 차를 모두 더한 것
# abs(x좌표 차이) + abs(y좌표 차이) 라는 뜻이므로
# 대각선으로 1,1 만큼 차이나면 맨해튼 거리는 2가 나오는것
# 해당 문제가 퍼즐이라는 것을 기억하면 "."은 퍼즐을 움직이기 위한 빈공간일것임
# 따라서 "."을 제외한 퍼즐중 본래 위치를 벗어난 것을 기존 위치와 비교하면
# "A":1,1 "F":1,1, "K":1,1 => "A":2, "F":2, "K":2
# 합치면 6이 나오게 된다
# 즉, "."을 제외한 퍼즐의 좌푯값 차이(절댓값)를 기록해서 합칠것
ini_array = ["ABCD", "EFGH", "IJKL", "MNO."]
array = [input() for _ in range(4)]
count = {}
result = 0
for i in range(4):
    for j in range(4):
        if array[i][j] != ini_array[i][j] and array[i][j] != ".":
            count[array[i][j]] = (i, j)
for i in range(4):
    for j in range(4):
        if ini_array[i][j] in count:
            result += abs(count[ini_array[i][j]][0] - i) + abs(count[ini_array[i][j]][1] - j)
print(result)