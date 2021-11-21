




# 런타임에러 및 반례 존재
"""
#  n 크기의 flag 리스트를 만들어 같은 열, 다른 행 마다 비교하여 중복 될 경우 + 해주는 방법?
# 처음 시도하려던 방식(최다 인덱스를 학년마다 기록하는 방식)은 두 개 이상의 값을 기록하지 못하는 문제가 있음
n = int(input())  # 행 길이
cls = [list(map(int, input().split())) for _ in range(n)]  # class, int 형태는 카운트 불가
cls_reverse = [[0 for _ in range(n)] for _ in range(5)]  # 각 학년마다 저장용
flag = [-1] * n  # 학년별 최다 중복반을 기록
for i in range(5):
    for j in range(n):
        cls_reverse[i][j] = cls[j][i]
for i in range(5):
    tmp_max = 1
    cls_idx = 0
    for j in range(n):
        tmp_max_cls = cls_reverse[i].count(cls_reverse[i][j])
        if tmp_max_cls > tmp_max:
            tmp_max = tmp_max_cls
            cls_idx = cls_reverse[i][j]
    if tmp_max != 1:
        flag[i] = cls_idx
# 여기까지 최댓값의 인덱스(반번호) 기록
student = [0] * n
for i in range(n):
    for j in range(i):
        if cls[i][j] == flag[j]:
            student[i] += 1
# 반장 중복시 낮은 번호의 학생을 추리기 위한 리스트
std_max = max(student)
std_idx = [i + 1 for i in range(n) if student[i] == std_max]
print(flag)
print(student)
print(std_idx)
# 반례
5
1 1 1 1 1
1 1 1 1 1
1 3 4 5 5
3 3 3 3 3
4 4 4 4 4
answer : 3
output : 1
"""
n = int(input())
cls = [list(map(int, input().split())) for _ in range(n)]
flag = [0] * n
for i in range(n):
    visited = [0 for _ in range(n)]
    for j in range(5):
        for k in range(n):
            if k != i and cls[k][j] == cls[i][j]:  # k != i : 자기 자신 제외
                visited[k] = 1
    flag[i] = len(list(filter(lambda x: x, visited)))
print(flag.index(max(flag)) + 1)