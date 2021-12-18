# 백준 11576
# a = N진수, b = M진수
a, b = map(int, input().split())
m = int(input())
array = list(map(int, input().split()))
array.reverse()
tmp = 0
result = []
# array에 나열된 a의 자릿수를 이용하여 N진수로 만들기
for i in range(m):
    tmp += array[i] * (a ** i)
# N 진수를 M 진수 자릿수로 변환하기
while tmp != 0:
    result.append(tmp % b)
    tmp //= b
print(*reversed(result))