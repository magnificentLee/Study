# 반복문을 사용할 경우 시간초과가 뜨게됨
# 따라서 단순한 계산식으로 생각해보자
"""
이익 = 판매가 - 생산원가 : 170 - 70 = 100
원금회수 = 고정비용 / 이익 : 1000 / 100 = 10
수익발생 = 10 + 1
b(생산원가) >= c(판매가) 인 경우 수익이 발생할 수 없음, 따라서 -1 출력
"""
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print((a // (c - b)) + 1)
# 아래는 시간초과가 발생하는 경우
"""
while True:
    total1 = a + (b * num)
    total2 = c * num
    if total1 == total2:  # 손익분기점
        num += 1  # 이득이 되는 시점
        print(num, total1, total2); break
    elif b > c:  # 이익이 절대로 날 수 없는 구조(적자만 늘어나는 구조)
        print(-1); break
    num += 1
"""