""" 소인수분해
a = int(input())
b = 2

while a != 1:
    if a % b == 0:
        a = a / b
        print(b)
    else:
        b += 1
"""
"""
n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    if a < b:
        a,b = b,a  # 유클리드 호제법: 큰 값이 앞에 와야 되기 때문

    res = b
    while res % a !=0:
        res += b

    print(res)
"""
# 최대공약수가 필요함
# 최대공약수 = 유클리드 호제법을 이용: 큰 수를 작은 수로 나누어 나머지를 구한다
# 예를 들어 192 72가 주어질때 192 % 72 = 48
# 72 % 48 = 24, 48 % 24 = 0 이므로 최대공약수는 24

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x = a
    y = b
    while b != 0:
        res = a % b  # 두 값을 나눈 나머지, 그 다음 뒷 값과 결과를 나눈 나머지
        a = b        # 참고로 while 문처럼 진행할시 큰 값이 자동으로 앞으로 이동하기 때문에 호제법을 사용 할 수 있다
        b = res  # res = result
    gcd = a  # 최대공약수
    lcd = x * y / a  # 최소공배수 : 두 값을 곱해서 최대공약수를 나눈게 최소공배수
    print(int(a), int(lcd))
