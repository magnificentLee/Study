n = int(input())
total_a = total_b = 100
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        total_b -= a
    elif a < b:
        total_a -= b
    else:
        pass
print(total_a, total_b)