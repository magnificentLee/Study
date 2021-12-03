# 중복 체크 때문에 고민하던차에 튜플도 set 가능한 것을 보고 이용
l = int(input())
x, y = 0, 0
graph = [(x, y)]
move = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
array = input()
for i in array:
    tmp_x, tmp_y = move[i]
    x += tmp_x
    y += tmp_y
    graph.append((x, y))
print(len(set(graph)))