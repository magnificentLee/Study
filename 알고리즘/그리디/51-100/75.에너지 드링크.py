# Xa + (Xb / 2) 로 만들고 b를 버리기 -> Xa 를 시작값, 가장 큰 값을 넣으면 결과=최댓값이 나올 것이다
from sys import stdin

input = stdin.readline

n = int(input())
drinks = sorted(map(int, input().split()), reverse=True)
result = drinks[0]
for i in range(1, n):
    result += drinks[i] / 2
print("%g" % result)