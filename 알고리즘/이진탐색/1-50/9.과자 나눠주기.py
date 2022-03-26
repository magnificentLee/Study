# 백준 16401 과자 나눠주기
# 과자의 길이는 길이순으로 입력됨(정렬 필요X)
# 과자 길이의 최댓값을 기준으로 절반으로 나눠가며
from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
array = list(map(int, input().split()))
start, end = 1, array[-1]  # array[-1]로 하면 바로 틀림, 왜 그런지는 모르겠음
result = 0
while start <= end:
    mid = (start + end) // 2  # 임시 길이 값
    tmp_m = 0  # 임시 인원 값 = 받아갈 수 있는 최대 인원수, 전체 인원수(m) 보다 많거나 같아야 결과로 쓸 수 있음
    for i in array:
        tmp_m += i // mid
    if tmp_m >= m:  # tmp_m = mid, m = target
        result = mid  # 헷갈리면 안 되는게 result는 최대 길이를 구하는거지 최대 인원을 구하는게 아님!
        start = mid + 1
    else:
        end = mid - 1
print(result)
# 1 1
# 1
# 을 입력시 zerodivision 에러가 발생
# 원인
# start 값을 0으로 설정해서 mid = (0 + 1) // 2 = 0
# 반복문을 진행하며 tmp_m = 1 // 0 , 따라서 에러가 발생
# 해결책
# start의 초기값을 1로 설정