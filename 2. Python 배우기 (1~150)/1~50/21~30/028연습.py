n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x = a
    y = b
    while b != 0:
        result = a % b
        a = b
        b = result
    gcd = a
    lcd = x * y / a
    print(int(gcd), int(lcd))
