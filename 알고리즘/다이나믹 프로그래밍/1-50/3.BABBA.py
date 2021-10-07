# A     :   1 0
# B     :   0 1
# BA    :   1 1
# BAB   :   1 2
# BABBA :   2 3
# 즉, 피보나치 방식
# 각각의 방식을 다시 확인해보면 a, b 전부 피보나치다
# A를 Na B를 Nb 라고 할 때 B는 Na - 1 번째
d = [0] * 46
d[1] = 1


def fibo(n):
    if n <= 1:
        return n
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]


k = int(input())
print(fibo(k - 1), fibo(k))
# 아래 방식은 메모리 초과 및 n = 45일 때 시간이 오래 걸리는 방식
# 아래 방식을 통해 알 수 있었던건 A,B 문자를 이용했기 때문에 메모리 초과가 발생
# A, B를 각각 함수를 작동시켜 카운트 했기 때문에 시간이 오래 걸렸던것으로 생각된다
"""
d = [0] * 46

def fibo(n):
    if n == 0:
        return "A"
    elif n == 1:
        return "B"
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]

k = int(input())
# A, B 각각 동작인데 좀더 효율적인 방법은?
A = fibo(k).count("A")
B = fibo(k).count("B")
print(A, B)
"""