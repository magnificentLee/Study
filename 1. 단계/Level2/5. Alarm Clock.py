"""
h, m = map(int, input().split())
if m < 45:
    if h == 0:
        m += 60
    else:
        h -= 1
        m += 60
print(h, m-45)
어차피 입력하는 값은 h: 0~23 / m: 0~59 m은 -45 이므로
"""
h, m = map(int, input().split())
if m < 45:
    if h == 0:
        h += 23
    else:
        h -= 1
    print(h, m + 15)
else:
    print(h, m - 45)
# h, m 이 양수인 상황 즉, h != 0 , m >= 45
# h, m 이 음수가 되는 상황을 고려하면 h == 0 , m < 45

