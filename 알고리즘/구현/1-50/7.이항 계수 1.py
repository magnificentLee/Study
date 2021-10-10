# 이항계수의 괄호안을 펼쳐보면 (위 아래) = 위C아래 로 나타낼 수 있다
# 이것은 팩토리얼로 나타내면 위! / (아래! * (위 - 아래)!)
def factorial(t):
    result = 1
    for i in range(1, t + 1):
        result *= i
    return result


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))