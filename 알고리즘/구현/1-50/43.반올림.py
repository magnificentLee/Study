# 반올림 = round 함수, 하지만 round 함수는 부동소수점 연산을 하기 때문에 불안정함
# 15 : 10 + 5, 5 >= 10 // 2
n = int(input())
m = 10
while True:
    if n < m:
        break
    if n % m >= m // 2:
        n += m
    n -= (n % m)
    m *= 10
print(n)