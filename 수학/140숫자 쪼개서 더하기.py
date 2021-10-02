"""
t = int(input())

n = list(map(int, input()))
print(sum(n))
"""
# 간단하게 줄여보자
t = int(input())

print(sum(list(map(int, input()))))
