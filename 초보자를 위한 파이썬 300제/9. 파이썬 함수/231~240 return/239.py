def 함수1(num):
    return num + 4

def 함수2(num):
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
# 계산 순서
# 함수2(10 + 2) -> num = 12 바인딩 -> 함수1 (12 + 4) = 16 반환