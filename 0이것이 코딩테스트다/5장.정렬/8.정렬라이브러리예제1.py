# 내 방법
"""
t = int(input())
nums = [int(input()) for i in range(t)]
nums.sort(reverse=True)
print(*nums)
"""
# 교재 방법
"""
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array = sorted(array, reverse=True)
for i in array:
    print(i, end=" ")
"""
# 숏코딩
print(*sorted([int(input()) for i in range(int(input()))], reverse=True))
