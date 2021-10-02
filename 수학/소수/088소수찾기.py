"""
n = int(input())
num_list = list(map(int, input().split()))


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:  # 예시 num = 7, 2~6으로 나누면 나머지 1이므로 True
            return False  # 예시 num = 6, 2~5로 나누면 나머지 0이므로 False
    return True  # return 값이 True 면 count 증가


count = 0
for i in num_list:
    if prime(i):
        count += 1
print(count)
"""
n = int(input())
num_list = list(map(int, input().split()))


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True  # return True : 함수 종료
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
for i in num_list:
    if prime(i):
        count += 1
print(count)
