# 백준 18917 수열과 쿼리 38
# XOR 연산 = 비트연산, 1 1을 비교하면 0이고 0 0 을 비교하면 0이며 0 1 을 비교하면 1이다
# 즉, 둘 중 하나만 참일때 만족
# a = 60, b = 13일 때
# a = 0011 1100
# b = 0000 1101
# (a ^ b) = 0011 0001
# 32+16+0+0+0+1 = 49
# 즉, a와 b의 XOR연산 결과는 49이다
# 0 3 1 4 : 3 + 1 + 4 = 8
# 0 3 1 4 : XOR연산을 해보면
# 0000 0011 0001 0010
# 0000 0011 = 0011
# 0011 0001 = 0010
# 0010 0100 = 0000
# 리스트를 이용하면 시간초과가 발생함 : 아래와 같이 변수에 바로 적용하는 방식을 사용해도
# 728ms 가 걸림, 당연히 시간초과가 발생함
from sys import stdin
input = stdin.readline

m = int(input())
result = 0
xor = 0
for _ in range(m):
    n = list(map(int, input().split()))
    if n[0] == 1:
        result += n[1]
        xor = xor ^ n[1]
    elif n[0] == 2:
        result -= n[1]
        xor = xor ^ n[1]
    elif n[0] == 3:
        print(result)
    else:
        print(xor)