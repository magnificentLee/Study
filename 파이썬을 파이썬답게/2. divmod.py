a, b = map(int, input().split())
# print(a // b, a % b)
print(*divmod(a, b))