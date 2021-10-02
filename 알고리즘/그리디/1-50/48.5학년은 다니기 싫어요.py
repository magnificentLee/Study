n, a, b = map(int, input().split())
credit = [list(map(int, input().split())) for i in range(10)]
count = 8 - n
for i in range(count):
    if credit[i][0] + credit[i][1] > 6:
        a += credit[i][0] * 3
        b += 6 * 3
    else:
        a += credit[i][0] * 3
        b += credit[i][0] * 3 + credit[i][1] * 3
    if a >= 66 and b >= 130:
        print("Nice")
        break
else:
    print("Nae ga wae")