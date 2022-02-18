# min을 총 3번 돌리면 되지 않을까? = > 문제를 잘못 파악함
# 1. case1 = min(전부 R로 바꾼 다음 B를 채우는 방법, 전부 B로 바꾼 다음 R을 채우는 방법)
# 2. case2 = min(count(B), count(R))
# 2. result = min(case1, case2)
# 여기까지 잘못 파악했던 내용
# 연속된 임의의 문제를 선택하여 바꾸는 것임
# 예제의 경우 BBRBRBBR 에서 BB/R/B/R/BB/R : 6, BBBBBBBB(1) + RRR(3) : 4 min(6, 4) = 4

n = int(input())
array = input()
a = array.split("B")
res1 = len(a) - a.count("") + 1
b = array.split("R")
res2 = len(b) - b.count("") + 1
print(min(res1, res2))
# print(res1)
# print(res2)
# 대충 반례의 경우가 있을 것 같아서 B, R이 우세인 경우를 나눠서 해봤는데 실제 반례에 있었음
# 6
# BRRRRB
# 인 경우
# res1 = 2, res2 = 3으로 실제 정답은 2임
# 우쨌든 최근 몇 달간 제출한 결과중에 제일 빨라서 다행임