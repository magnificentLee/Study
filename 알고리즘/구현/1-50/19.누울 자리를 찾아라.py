# 이해하는데 시간이 걸린 문제로 제대로 읽지 않은게 큼
# 2칸 이상일때 벽에 닿았을 경우 1개 카운트
# .일 경우 계속 진행하고 x가 나오면 카운트후 다음 반복문으로 진행
def row():  # 행 : 가로 ->
    result = 0
    for i in range(n):
        count = 0
        for j in range(n + 1):
            if room[i][j] == ".":
                count += 1
            else:
                if count >= 2:
                    result += 1
                count = 0
    return result

def col():  # 열 : 세로 ↓
    result = 0
    for i in range(n):
        count = 0
        for j in range(n + 1):
            if room[j][i] == ".":
                count += 1
            else:
                if count >= 2:
                    result += 1
                count = 0
    return result


n = int(input())
room = [input() + "X" for _ in range(n)] + ["X" * (n + 1)]  # 방의 오른쪽, 아래는 벽(종료 조건)
print(row(), col())