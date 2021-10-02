def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


t = int(input())
n_list = map(int, input().split())
count = 0
for i in n_list:
    if prime(i):
        count += 1
print(count)