n = int(input())
n_list = list(map(int, input().split()))
count = 0


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:  # 1 과 자기자신을 제외한 약수가 존재하는 경우
            return False
    return True


for i in n_list:
    if prime(i):
        count += 1
print(count)
