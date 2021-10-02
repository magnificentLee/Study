# 1. 시간초과
"""
def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for j in range(n + 1, 2 * n + 1):  # n보다 크다 = 초과
        if prime(j):
            count += 1
    print(count)
"""
# 2. 성공
"""
def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


num_list = list(range(2, 246912))
prime_list = []
for i in num_list:
    if prime(i):
        prime_list.append(i)

while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    for i in prime_list:
        if n < i <= n * 2:
            count += 1
    print(count)
"""
# 100000 의 연산시간 = 3~3.5초 나머지를 합치면 대략 10초
# 일반적으로 코딩테스트는 1~5초 의 제한시간을 가지고 이를 넘어가면 오답처리 된다.
# 매번 입력할 때 마다 소수를 세는 경우 시간초과가 발생한다
