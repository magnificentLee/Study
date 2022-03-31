# 백준 20125 쿠키의 신체 측정
# 좀더 다듬으면 깔끔할것 같음
# * 이면 상하좌우 체크, 상하좌우가 *이라면 인덱스 저장 (심장)
# 심장위치의 행을 이용하면 팔의 길이를 알 수 있을 것
# 심장위치의 열을 이용하면 허리의 길이를 알 수 있을 것
# 심장은 머리와 1칸 떨어짐
# 팔은 심장이 있는 행, 심장의 열 - 시작지점 열, 심장의 열 - 끝부분 열?
# n * n 행렬
# 출력 순서 : 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
n = int(input())
a = [input() for _ in range(n)]
idx_h, jdx_h = 0, 0
flag = 0
for j in range(n):
    for i in range(n):
        if a[j][i] == "*":
            jdx_h = j + 1
            idx_h = i
            print(jdx_h + 1, idx_h + 1)
            flag = 1
            break
    if flag:
        break
# 팔 길이 측정 arms[좌,우]
result = []
# 왼쪽 팔
for i in range(n):
    if a[jdx_h][i] == "*":
        result.append(idx_h - i)
        break
# 오른쪽 팔
for i in range(n - 1, -1, -1):
    if a[jdx_h][i] == "*":
        result.append(i - idx_h)
        break
# 허리
for j in range(n - 1, -1, -1):
    if a[j][idx_h] == "*":
        result.append(j - jdx_h)
        break
# 다리
left_leg_string = ""
right_leg_string = ""
left_leg_length = 0
right_leg_length = 0
for j in range(n):
    left_leg_string += a[j][idx_h - 1]
    right_leg_string += a[j][idx_h + 1]
for i in left_leg_string.split("_"):
    left_leg_length = max(left_leg_length, i.count("*"))
result.append(left_leg_length)
for i in right_leg_string.split("_"):
    right_leg_length = max(right_leg_length, i.count("*"))
result.append(right_leg_length)
print(*result)