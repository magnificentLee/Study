a, b = map(int, input().split())
x = a
y = b
while b != 0:
    result = a % b
    a = b
    b = result
gcd = a  # 최대공약수
lcd = x * y // a  # 최소공배수
print(gcd, lcd, sep="\n")