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
def prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i 이후 i 의 배수들을 False판정
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]  # 소수목록 산출

print(prime_list(10000))