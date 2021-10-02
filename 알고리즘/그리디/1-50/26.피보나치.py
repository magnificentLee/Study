# 시간제한, 숫자의 범위 때문에 리스트화로는 안 될 것으로 추정
from sys import stdin
fibo = [0, 1]
for i in range(2, 50):
    # 2, 46 도 가능 : fibo[45] = 1134903170 ~= 11억
    # n 의 범위가 10억까지기 때문
    fibo.append(fibo[i - 2] + fibo[i - 1])

t = int(stdin.readline())

for j in range(t):
    n = int(stdin.readline())

    array = []

    while(n):
        for k in range(50):
            if fibo[k] <= n:
                m = fibo[k]

        n = n - m
        array.append(m)
        array.sort()

    for l in array:
        print(l, end=" ")
    print("")