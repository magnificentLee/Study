""" 기존 소수 판별함수
1.
def prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
2. 빠른 소수 판별법(소수는 해당 수의 절반까지만 나온다는 점에서 착안)
def prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True
3. 더 빠른 소수 판별법(해당 수의 제곱근까지만 알아봐도 되는 방법)
def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
"""
