# 별 이후엔 공백이 필요없다는 점에 유의할것
n = int(input())
a = n
for i in range(n - 1):
    print(" " * i + "*" * (2 * (a - i) - 1))

for j in range(1, n + 1):
    print(" " * (a - j) + "*" * (2 * j - 1))
