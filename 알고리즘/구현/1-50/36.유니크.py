# 전체리스트를 비교하는게 아니고 리스트의 각 인덱스별로 비교하는 것임
# 중복 될 경우 0 처리, 아니면 +처리
# pop으로 처리하려고 했으나 max값이 중복될 경우 pop 하는 방법이 떠오르지 않음
t = int(input())
players = [[], [], []]
result = []
for _ in range(t):
    a, b, c = map(int, input().split())
    players[0].append(a)
    players[1].append(b)
    players[2].append(c)
for i in range(t):
    tmp_result = 0
    for j in range(3):
        if players[j].count(players[j][i]) == 1:
            tmp_result += players[j][i]
    result.append(tmp_result)
print(*result, sep="\n")