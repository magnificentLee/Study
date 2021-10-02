n = int(input())
result = 0

while True:
    if n < 0:
        break
    if n % 5 == 0:
        result += n // 5
        break
    else:
        n -= 2
        result += 1
# n >= 0 || n < 0
if n >= 0:
    print(result)
else:
    print(-1)