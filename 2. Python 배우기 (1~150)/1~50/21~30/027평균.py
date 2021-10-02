# 10039번
# 입력은 총 5줄, 점수는 모두 0점 이상, 100점 이하인 5의 배수, 평균 점수는 항상 정수
a_list = []

for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    a_list.append(a)
avg = sum(a_list) / len(a_list)
print(int(avg)) # int가 없을경우 68.0 이 나옴 자릿수에 주의할 것.
