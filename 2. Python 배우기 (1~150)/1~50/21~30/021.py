# 첫째 줄에 양의 정수 A가 주어진다.
#
# 둘째 줄에 연산자 + 또는 *가 주어진다.
#
# 셋째 줄에 양의 정수 B가 주어진다.
#
# A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.

a = int(input())
b = input()
c = int(input())

if b == "+":
    print(a + c)
elif b == "*":
    print(a * c)
else:
    print("연산자를 제대로 입력하시오")
