# 시도1 : 성공
"""
t = int(input())
n = list(input())
result = 0
for i in n:
    result += int(i)
print(result)
"""
n = int(input())
print(sum(list(map(int, input()))))