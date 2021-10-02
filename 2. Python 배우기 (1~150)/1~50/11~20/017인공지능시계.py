# 첫줄 시, 분, 초 입력
# 둘줄 필요한 시간(초)
# 출력: 시 분 초
""" 첫 시도 = 실패, 최댓값을 넣을시 시간이 100시간을 넘어가버림
h, m, s = map(int, input().split())
t = int(input())
sum = h * 3600 + m * 60 + s + t
if sum >= 86400:
    sum -= 86400
if sum // 3600 >= 86400:
print("{} {} {}".format(sum // 3600, (sum // 60) % 60, sum % 60))
"""
a, b, c = map(int, input().split())
estimateTime = int(input())

# 예상 완료시각
a += estimateTime // 3600
b += (estimateTime // 60) % 60
c += estimateTime % 60

# 디지털 시각으로 변환
if c >= 60:
    c -= 60
    b += 1
if b >= 60:
    b -= 60
    a += 1
if a >= 24: # 초 - 분 - 시 순으로 진행되기 때문
    a = a % 24
print(a, b, c)
