# 24 18 or 18 24
# 최대공약수, 최대공배수
a, b = map(int, input().split())
x = a
y = b
while b != 0:
    result = a % b
    a = b
    b = result
gcd = a
lcd = x * y // a
print(gcd, lcd, sep="\n")