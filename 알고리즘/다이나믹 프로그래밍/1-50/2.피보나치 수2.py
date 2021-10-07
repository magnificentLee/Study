d = [0] * 100

def fibo(n):
    if n <= 1:
        return n
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]


n = int(input())
print(fibo(n))