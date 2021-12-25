# 중복되지 않는 값만 입력된다는 조건이 없음 -> 집합 형태로 길이 확인할것
# 1. 중복 방문 확인 -> 방문 안 한 곳이 생기게 된다. 나이트 투어 조건을 만족하지 못한다.
#
# 2. 마지막 위치에서 첫 번째 위치를 못 가는 경우.
#
# 3. 경로 중 A위치에서 B위치로 가는 도중, 갈 수 없는 경우. 검사 조건은 2번과 동일.
# 문제에서 중간 경로가 잘못될 수 있다는 조건이 없어서 처음에 생각하지 못한 조건.
# (다음 값의 영어 - 현재 값의 영어) * (다음 값의 숫자 - 현재 값의 숫자) = 이동거리
# 이동거리는 2(나이트이기 때문에), 2가 아니라면 invalid
# 리스트의 역순으로 진행하여 마지막 값이 시작값과 동일하면 valid?
array = [input() for _ in range(36)]
dy = [1, -1, 1, -1, 2, -2, 2, -2]  # y축 i[dy][dx]
dx = [2, 2, -2, -2, 1, 1, -1, -1]  # x축
if len(set(array)) == 36:
    for i in range(35):
        if abs((ord(array[i][0]) - ord(array[i + 1][0])) * ((int(array[i][1])) - int(array[i + 1][1]))) != 2:
            print("Invalid")
            break
    else:
        for j in range(8):
            ny = int(array[i + 1][1]) + dy[j]
            nx = ord(array[i + 1][0]) + dx[j]
            if 1 <= ny <= 6 and ord("A") <= nx <= ord("Z"):  # 인덱스 0,0 의 값은 정확히는 a1 이기 때문에
                if chr(nx) == array[0][0] and ny == int(array[0][1]):
                    print("Valid")
                    break
        else:
            print("Invalid")
else:
    print("Invalid")