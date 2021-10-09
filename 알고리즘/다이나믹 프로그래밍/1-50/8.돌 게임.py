# 그리디에서 풀던 방식으로 풀어봤는데 맞았다
# 다이나믹 프로그래밍이라고 무조건 새로운 방식으로 접근하는건 아닌가보다
n = int(input())

result = 0

while n > 0:
    if n % 3 == 0:
        result += n // 3
        break
    n -= 1
    result += 1
if result % 2 != 0:
    print("SK")
else:
    print("CY")

# 찾아보니 훨씬 더 간단한 방법도 있다
"""
n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")
"""