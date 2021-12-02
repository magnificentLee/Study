# 카약의 번호는 순서임 i 번째 팀이라는 뜻이고 입력 받는 순서는 상관 없음
# 출력은 i번째 줄 = i번 팀의 등수
# 각 열의 행들을 비교하여 "."이 아니고 방문한적이 없다면 현재 인덱스에 순위를 입력하여 방문처리
# 이후로 방문됐다면 등급을 올리고 아니라면 인덱스에 순위 입력
r, c = map(int, input().split())
array = [input() for _ in range(r)]
idx = [0] * 10  # 출력값은 9개만 나오면 됨
grade = 1
for i in range(c - 2, 0, -1):
    flag = 0
    for j in range(r):
        if array[j][i] != "." and idx[int(array[j][i])] == 0:
            idx[int(array[j][i])] = grade
            flag = 1
    if flag == 1:  # 방문했으면
        grade += 1
for i in idx:
    if i != 0:
        print(i)