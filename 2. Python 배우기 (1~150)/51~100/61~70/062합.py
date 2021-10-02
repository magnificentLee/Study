"""
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)
"""
# 간단한 수학상식 a*(a+1)//2 = 1부터 a까지의 합
a = int(input())
print(a*(a+1)//2)