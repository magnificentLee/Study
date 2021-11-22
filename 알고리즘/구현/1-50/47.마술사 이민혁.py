# append만 쓰다보니 extend 라는 함수가 있다는걸 까먹음
def error(a, b, array):
    a -= 1  # 인덱스상 -1, 아니면 인덱스 초과
    b -= 1
    if array[a][b] == "#":
        array[a][b] = "."
    else:
        array[a][b] = "#"
    return array


r, c = map(int, input().split())
up = [list(input()) for _ in range(r)]
a, b = map(int, input().split())
for i in up:
    i.extend(i[::-1])
down = []
for i in reversed(up):
    down.append(list(i))
# down = list(reversed(up)) 원래 했던 부분으로 위아래가 동일하게 바뀌는 문제가 있었음
# 함수 부분을 result 취합 밑으로 if문으로 고쳐 넣는 방식을 써도 똑같은 문제가 생겼음
# #..# 이 아닌     #..# 와 같은 방식으로 나왔음
# .##.            .#..
# .#..            .#..
# #..#            #..#
# 내가 생각엔 순서에 상관없이 컴퓨터 메모리에 먼저 접근하는 바람에 꼬여버린것 같음
result = up + down
for i in error(a, b, result):
    print(*i, sep="")