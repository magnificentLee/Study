h, m = map(int, input().split())

if m < 45:
    m += 15
    if h == 0:
        h += 23
        print(h, m)
    else:
        h -= 1
        print(h, m)
else:
    m -= 45
    print(h, m)