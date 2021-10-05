# 수강인원 대비 신청자수가 적을 때 : 마일리지 1 적립
# 각 점수 리스트를 내림차순으로 정렬하여 인덱스 l - 1 즉, 가장 마지막 번째의 수(가장 작은수)를 리스트에 저장
# 리스트에 저장된 값들을 오름차순으로 정렬하여 만약 주어진 마일리지 값을 초과한다 : 마지막수 pop(가장 큰 수)
# 초과하지 않는다 : len(리스트) : 과목 개수, 따라서 정답일 것
n, m = map(int, input().split())
miles_list = []

for _ in range(n):
    p, l = map(int, input().split())  # 신청자, 수강 총인원
    miles = sorted(map(int, input().split()), reverse=True)
    if p < l:
        miles_list.append(1)  # 마일리지 1로도 만족하기 때문
    else:
        miles_list.append(miles[l - 1])  # 가장 작은값(값이 같아도 우선순위가 높기 때문) 추가
miles_list.sort()  # pop()은 가장 오른쪽부터 빠지기 때문
while miles_list:
    if sum(miles_list) > m:  # 주어진 마일리지를 초과할 때
        miles_list.pop()  # 가장 큰 값 제거
    else:
        break  # 만족하면 반복문 탈출
print(len(miles_list))