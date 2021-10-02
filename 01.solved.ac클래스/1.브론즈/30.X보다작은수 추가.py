a, b = map(int, input().split())
nums = list(map(int, input().split()))
result = [i for i in nums if i < b]
print(*result)