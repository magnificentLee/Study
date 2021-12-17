# 대각선 처리를 어떻게 해야하나 고민하는중
# 대각선 X : 즉, 두 개로 나눠서 확인
# 전체 빙고의 개수가 아닌 빙고 3개를 만들면 종료
def check(v):
    n = 0
    # 가로
    for i in range(5):
        flag = True
        if False in v[i]:
            flag = False
        if flag:
            n += 1
    # 세로
    col_v = list(map(list, zip(*v)))
    for i in range(5):
        flag = True
        if False in col_v[i]:
            flag = False
        if flag:
            n += 1
    # 대각선
    ltor_flag, rtol_flag = True, True
    for i in range(5):
        if v[i][i] == 0:
            ltor_flag = False
        if v[i][4 - i] == 0:
            rtol_flag = False
    if ltor_flag:
        n += 1
    if rtol_flag:
        n += 1
    if n >= 3:
        return True
    return False


array = [list(map(int, input().split())) for _ in range(5)]
target = [list(map(int, input().split())) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
result = 0
for i in target:
    while i:
        n = i.pop(0)
        result += 1
        for j in range(5):
            for k in range(5):
                if array[j][k] == n:
                    visited[j][k] = True
                    break
        if result >= 5 and check(visited):
            print(result)
            exit()
