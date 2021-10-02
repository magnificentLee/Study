# 동전의 종류
# 쿼터 다임 니켈 페니
# 0.25 0.10 0.05 0.01 (1달러기준)
# 거스름돈은 항상 5달러 이하, 동전의 개수를 최소화
# 첫 시도 : 성공
"""
q, d, n, p = 0, 0, 0, 0  # 25, 10, 5, 1
t = int(input())
for _ in range(t):
    m = int(input())  # money
    q = m // 25
    m %= 25

    d = m // 10
    m %= 10

    n = m // 5
    m %= 5

    p = m // 1
    m %= 1
    print(q, d, n, p)
"""
# 두번째 : 간단하게 줄이기
t = int(input())

for _ in range(t):
    money = int(input())
    coin = {25: 0, 10: 0, 5: 0, 1: 0}
    while money:
        for num in [25, 10, 5, 1]:
            while money >= num:
                money -= num
                coin[num] += 1
    print(coin[25], coin[10], coin[5], coin[1])