n = int(input())
m = 0
for i in range(n+1):
    m = m + i
print(m)
"""
i 는 시작값으로 1
n+1 = 종료값, range에서 종료값은 자기 자신을 포함하지 않기 때문에 +1을 해준다
따라서 m = 0 + 1 =1, m = 1 + 2 =3, m = 3 + 3=6
"""
"""
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
"""