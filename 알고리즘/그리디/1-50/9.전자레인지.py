# 개선한 풀이 68ms
# 본격적인 계산전에 나머지가 있는지(즉, 나누어 떨어지지 않는지) 파악하여 바로 출력
# 아닌 경우 계산
n = int(input())
if n % 10 != 0:
    print(-1)
else:
    a, b, c = 0, 0, 0
    a += n // 300
    n %= 300

    b += n // 60
    n %= 60

    c += n // 10
    n %= 10
    print("{} {} {}".format(a, b, c))
# 첫 풀이
# 쓸 때 없는 계산 때문에 시간이 더 걸림:92ms
"""
n = int(input())
a, b, c = 0, 0, 0
a += n // 300
n %= 300
b += n // 60
n %= 60
c += n // 10
n %= 10
if n == 0:
    print("{} {} {}".format(a, b, c))
else:
    print(-1)
"""