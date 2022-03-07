# 절사평균
# 극단적인 값들이 평균을 왜곡하는 것을 막기 위해 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것을 말한다.
# 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다.
# 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다.
# 반올림 처리가 문제
# 전체의 개수 n = 0도 가능하므로 0일 때의 예외도 처리
# 처음 제외 인원수를 구할 때 1번, 평균을 구하면서 1번 : 총 2번의 반올림을 해야되므로 함수를 만들어서 처리하는게 나을 것임
from sys import stdin
input = stdin.readline
def rnd(e):
    tmp = e - int(e)  # 소수 계산
    if tmp >= 0.5:
        e = int(e) + 1
    else:
        e = int(e)
    return e


n = int(input())
if n == 0:
    print(0)
else:
    array = sorted([int(input()) for _ in range(n)])
    exception = rnd(n * 0.15)  # 전체 인원수 * 0.15(15%) = 평균계산에서 제외할 인원수
    # int(tmp) 에서 int(0.4) = 0 : 아무도 제외X, 예외에 주의
    # array[0:-0] 은 0이므로 exception이 0이 아닌 경우의 예외처리, 그 외에는 전체를 더하게 끔
    if exception != 0:
        up = sum(array[exception:-exception])
    else:
        up = sum(array)
    result = rnd(up / (n - exception * 2))
    print(result)
