# 백준 18110 solved.ac (절사평균 문제)
# 절사평균 : 절사평균값 mean 만큼 앞 뒤를 짤라서 나머지만 계산하는 것
# mean = 1이라면 array = [2, 4, 6, 8, 9] 에서 2, 9 를 제외, sum([4, 6, 8]) / (len(array) - mean * 2) 의 값임
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
    if exception != 0:
        up = sum(array[exception:-exception])
    else:
        up = sum(array)
    result = rnd(up / (n - exception * 2))
    print(result)