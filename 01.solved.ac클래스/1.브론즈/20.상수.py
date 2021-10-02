"""
a, b = input().split()
n = (a[::-1], b[::-1])
print(max(n))
"""
# 숏코딩
print(max([int(i[::-1]) for i in input().split()]))