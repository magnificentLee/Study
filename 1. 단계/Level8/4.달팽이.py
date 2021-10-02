# 길이가 10억까지 가기 때문에 시간초과가 발생한다
"""
a, b, v = map(int, input().split())
old_total = 0
day = 0
while True:
    total = old_total + a
    day += 1
    if total >= v:
        break
    total -= b
    old_total = total
print(day)
"""
a, b, v = map(int, input().split())
if (v - b) % (a - b) != 0:
    print((v - b)//(a - b) + 1)
else:
    print((v - b)//(a - b))