# 1, 1, 2, 3, 5, 8, ...

def 피보나치(n):
    if n <= 1:
        return n
    else:
        return 피보나치(n - 1) + 피보나치(n - 2)


for i in range(1, 11):
    print(피보나치(i))
