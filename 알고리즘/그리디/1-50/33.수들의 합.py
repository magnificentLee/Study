s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
# 숏코딩
# print(int((-1 + (1 + 8 * int(input())) ** 0.5)/2))
