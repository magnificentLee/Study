# 테스트케이스개수
# 수강생 수
# 수강생의 참가자 번호
# 대회의 참가자 수
# 각 참가자의 마라톤 결과
# 참가자 번호, 기록(시간) 기록(분)
# 중간에 포기한 경우 -1 -1로 표시
# 0을 제거할때 발생하는 인덱스 초과 때문에 입력할 때 최대 초과(4920 초과)를 입력하여 제일 뒤로 빼게 바꿨음
from sys import stdin
input = stdin.readline

for _ in range(int(input())):  # 테스트 케이스 수, 반복문 통합
    parts = [[0, 0, 0] for _ in range(int(input()))]  # 수강생 수, 반복문 통합
    array = list(map(int, input().split()))
    idx = 0
    count = 0
    for i in range(int(input())):  # 참가자 수, 반복문 통합
        a, b, c = map(int, input().split())
        if a in array:
            if b != -1:
                tmp = b * 60 + c  # 전체 소요시간(분)
                parts[idx][0] = a
                parts[idx][1] = tmp
                parts[idx][2] = i + 1  # 값이 중복될 경우 우선순위 판별을 위한 값, 0과의 구별을 위해 1부터 시작
                if tmp <= 360:  # 기록이 6시간 이하인 경우 인증서 지급, 카운트
                    count += 1
            else:  # 중도 탈락하는 경우
                parts[idx][0] = a
                parts[idx][1] = 5000  # 최대 초과, 가장 뒤로 가게끔, h <=23, m <= 59 즉, 최대 4920분
                parts[idx][2] = i + 1
            idx += 1
    parts.sort(key=lambda x: (x[1], x[2]))
    print(parts[0][0], count)

# 처음 풀었던 방식 정답임, 시간 오래걸림
"""
for _ in range(int(input())):
    k = int(input())  # 수강생 수
    array = list(map(int, input().split()))
    n = int(input())  # 참가자 수
    parts = [[0, 0, 0] for _ in range(k)]
    idx = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if a in array:
            if b != -1:
                tmp = b * 60 + c  # 전체 소요시간(분)
                parts[idx][0] = a
                parts[idx][1] = tmp
                parts[idx][2] = i + 1  # 값이 중복될 경우 우선순위 판별을 위한 값, 0과의 구별을 위해 1부터 시작
            else:  # 중도 탈락하는 경우
                parts[idx][0] = a
                parts[idx][1] = 5000  # 최대 초과, 가장 뒤로 가게끔, h <=23, m <= 59 즉, 최대 4920분
                parts[idx][2] = i + 1
            idx += 1
    parts.sort(key=lambda x: (x[1], x[2]))
    count = 0
    for i in range(k):
        if parts[i][1] <= 360:  # 인증서 : 6시간 이하인 경우
            count += 1
    print(parts[0][0], count)
"""