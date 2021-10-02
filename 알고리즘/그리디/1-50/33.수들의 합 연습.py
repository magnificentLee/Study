# 초기
"""
n = int(input())
half = n // 2
m = 0
result = 0

for i in range(1, half + 1):
    m += i
    result += 1
    if n < m:
        result -= 1
        break
print(result)
"""
# 어차피 절반 즈음에 해결되므로 알아서 탈출할 것임
n = int(input())
m = 0
result = 0
for i in range(1, n + 1):
    m += i
    result += 1
    if n < m:
        result -= 1
        break
print(result)