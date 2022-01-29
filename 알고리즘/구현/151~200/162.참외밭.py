# 육각형이므로 총 6개의 변만 입력 받음
# 1번 카운트 되는 변들의 곱 = 큰 사각형
# 한 변을 기준으로 앞 뒤 변의 길이의 합이 최대와 같다면 파인지점
# 앞 뒤 길이의 측정 : 전체 길이 6, 인덱스는 5이므로
# 인덱스 0과 인덱스5의 앞뒤까지 비교하려면 (i + 5) % 6, (i + 1) % 6  : 인덱스0부터 끝까지 찾을때의 경우
# 단순히 인덱스 +2, +3 으로 찾으면 인덱스 에러가 발생할것임
# 특정 인덱스 앞뒤를 [(i-1) % 6, (i+1) % 6] 빼주면 작은 사각형의 가로, 세로가 나올 것
k = int(input())
array_dir = []
array_length = []
w, h = 0, 0
x, y = 0, 0
for i in range(6):
    dir, length = map(int, input().split())
    if dir == 1 or dir == 2:  # 동, 서
        if w < length:
            w = length
    elif dir == 3 or dir == 4:  # 남, 북
        if h < length:
            h = length
    array_dir.append(dir)
    array_length.append(length)
for i in range(6):  # array_length의 길이는 항상 6임
    if (array_dir[i] == 1 or array_dir[i] == 2) and h == array_length[(i + 5) % 6] + array_length[(i + 1) % 6]:
        x = array_length[i]
    elif (array_dir[i] == 3 or array_dir[i] == 4) and w == array_length[(i + 5) % 6] + array_length[(i + 1) % 6]:
        y = array_length[i]
result = k * (w * h - x * y)
print(result)