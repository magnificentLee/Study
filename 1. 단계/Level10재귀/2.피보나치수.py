# n = 17 일 때
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# 55, 89, 144, 233, 377, 610, 987, 1597
# 방법1
"""
n = int(input())
a = 0
b = 1
c = 0
for i in range(n):
    c = a
    a = b
    b = c + b
print(a)
"""
# 방법2
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(int(input())))