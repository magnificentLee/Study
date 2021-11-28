# 문제를 복잡하게 생각했지만 전혀 아님
# 제일 위를 출입구라 생각해서 후진하는 각도까지 생각해야 하나 했지만 전혀 아니고
# 2*2 범위만 체크하면 되는거였음
r, c = map(int, input().split())
array = [input() for _ in range(r)]
res0, res1, res2, res3, res4 = 0, 0, 0, 0, 0
for i in range(r - 1):
    for j in range(c - 1):
        count = 0
        countX = 0
        for x in range(i, i + 2):
            for y in range(j, j + 2):
                if array[x][y] == "#":
                    break
                elif array[x][y] == ".":
                    count += 1
                elif array[x][y] == "X":
                    countX += 1
        if count == 4:
            res0 += 1
        elif count >= 3 and countX == 1:
            res1 += 1
        elif count >= 2 and countX == 2:
            res2 += 1
        elif count >= 1 and countX == 3:
            res3 += 1
        elif countX == 4:
            res4 += 1
print(res0, res1, res2, res3, res4, sep="\n")