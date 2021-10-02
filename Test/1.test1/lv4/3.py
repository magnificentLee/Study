a = b = int(input())
n = 0
while True:
    ten = a // 10
    one = a % 10
    total = ten + one
    a = int(str(one) + str(total % 10))
    n += 1
    if a == b:
        break
print(n)
