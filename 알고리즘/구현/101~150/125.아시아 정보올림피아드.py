# 3명에게 메달을 주며 같은 팀의 중복은 최대 2개까지만 허용하므로
# 1등의 팀을 카운트하여 두번을 넘어가면 작동하게 하면 될 것 같다
from sys import stdin
input = stdin.readline

array = []
for _ in range(int(input())):
    c, n, s = map(int, input().split())  # country, number, score
    array.append((c, n, s))

array.sort(key=lambda x: x[2], reverse=True)
count, tmp, idx = 0, 0, array[0][0]
for i in array:
    if count == 3:
        break
    if i[0] == idx:
        tmp += 1
        if tmp > 2:
            continue
        else:
            count += 1
            print(i[0], i[1])
    else:
        count += 1
        print(i[0], i[1])