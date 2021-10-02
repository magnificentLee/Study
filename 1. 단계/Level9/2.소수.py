a = int(input())
b = int(input())
n = []


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
        n.append(i)
if len(n) >= 1:
    print(sum(n), min(n), sep="\n")
else:
    print(-1)
