"""
num, base = map(int, input().split())
if base == 3:
    ten = num // 10
    one = num % 10
    total = ten + one
elif base == 5:
"""
"""
num, base = map(int, input().strip().split(' '))
str_num = str(num)
answer = int(str_num, base)
print(answer)
"""
"""
num, base = map(int, input().split())
str_num = str(num)
answer = int(str_num, base)
print(answer)
"""
"""
num = "444"
base = 5
result = 0
for idx, i in enumerate(num[::-1]):  # num
    result += int(i) * (base ** idx)
    print(idx, i)
print(result)
"""
# 프로그래머스 솔루션
"""
num, base = map(int, input().strip().split(" "))
result = 0
for i in range(len(str(num))):
    result += int(str(num)[-1-i]) * (base ** i)
print(result)
"""
# 파이썬에서 제일 쉬운 방법
num = "444"
base = 5
result = int(num, base)
print(result)