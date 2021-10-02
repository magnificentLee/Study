a = int(input())
b = int(input())
data = []


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
        data.append(i)
if len(data) == 0:
    print(-1)
else:
    print(sum(data),min(data), sep="\n")
