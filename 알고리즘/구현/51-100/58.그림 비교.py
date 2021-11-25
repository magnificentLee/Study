# 서로 다른 칸의 갯수가 가장 작은 경우 = 가장 비슷함
t = int(input())
pic = []  # 3차원 리스트
min_val = 35  # 다를 수 있는 최대의 갯수
result = [0] * 2
for _ in range(t):
    row = [input() for _ in range(5)]
    pic.append(row)
for x in range(t):
    for y in range(x + 1, t):  # range(n, n) 일땐 공백인것을 생각하여 작성
        count = 0  # 1행과 2,3,4.. 행 비교, 2행과 3,4.. 비교하는 식으로 진행하기 때문
        for i in range(5):
            for j in range(7):
                if pic[x][i][j] != pic[y][i][j]:
                    count += 1
        if min_val >= count:
            min_val = count
            result[0] = x + 1  # 인덱스라서 +1
            result[1] = y + 1
print(*result)