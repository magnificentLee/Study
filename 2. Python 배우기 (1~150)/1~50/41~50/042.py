m, f = map(int, input().split())
total = 0
while m and f != 0:
    total = m + f
    print(total)
    m, f = map(int, input().split())