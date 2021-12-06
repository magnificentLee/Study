# 8 2 0 : 8명이 있는 곳에서 2번째 등장하는 0을 찾으라는 말  (0:뻔,1:데기)
# 뻔데기 순서는 [0 1 0 1] 기본 + [0] * n회째 + [1] * n회째
# 0 1 0 1 0 0 1 1 / 0 1 0 1 0 0 0 1 1 1 / ...
# 0, 1 은 길이의 절반
a = int(input())
t = int(input())
target = int(input())
array = []
total, count = 0, 0
repeat = 2  # 초기 2회  (뻔 데기 뻔 데기 뻔 뻔 데기 데기)
while True:
    array += [0, 1, 0, 1]  # 기본구조
    array += [0 for _ in range(repeat)]
    array += [1 for _ in range(repeat)]
    if count == t:
        break
    l = len(array)
    if l // 2 >= t:
        for i in range(l):
            total += 1
            if array[i] == target:
                count += 1
                if count == t:
                    break
    repeat += 1
idx = (total % a) - 1  # 이대로 끝내면 음수가 나오는 경우가 생김
players = [i for i in range(a)]
print(players[idx])