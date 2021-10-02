# 3 16
# 3 5 7 11 13
# 시간초과
"""
a, b = map(int, input().split())


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(a, b + 1):
    if prime(i):
        print(i)
"""
# 소수의 원리를 찾자
# 어떤 수는 절반 값까지만 약수를 가질 것이다
# 120이 주어지면 60을 넘어간 수에선 약수가 없다
# 1. 따라서 절반까지만 찾아도 시간을 절약할 수 있다 -> 생각보다 오래걸림
# 2. i의 제곱값으로 확인하는 방법
# 3964ms
a, b = map(int, input().split())


def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지이므로 +1
            if num % i == 0:
                return False
        return True


for i in range(a, b + 1):
    if prime(i):
        print(i)