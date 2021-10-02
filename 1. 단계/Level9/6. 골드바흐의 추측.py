# 에라토스테네스의 체를 이용해보자
prime = [True] * 10001
for i in range(2, int(10001 ** 0.5) + 1):
    if prime[i] == True:
        for j in range(i + i, 10001, i):
            prime[j] = False
prime_list = [i for i, j in enumerate(prime) if j == True and i >= 2]

gold = [[] for _ in range(10001)]

for i in range(len(prime_list)):
    for j in range(i, len(prime_list)):
        even_num = prime_list[i] + prime_list[j]
        if even_num % 2 == 0 and even_num <= 10000:
            gold[even_num].append([prime_list[i], prime_list[j]])
t = int(input())

for _ in range(t):
    n = int(input())
    result = [0, 0]

    for [i, j] in gold[n]:
        if i * j > result[0] * result[1]:
            result[0] = i
            result[1] = j
    print("{} {}".format(result[0], result[1]))
"""
prime = [0 for i in range(10001)]
prime[1] = 1
for i in range(2, int(i ** 0.5)):
    for j in range(i + i, 10001, i):
        prime[j] = 1

t = int(input())
for i in range(t):
    n = int(input())
    m = n // 2
    for j in range(m, 1, -1):
        if prime[n - j] == 0 and prime[j] == 0:
            print(j, n - j)
            break
"""