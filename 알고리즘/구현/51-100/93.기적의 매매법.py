# 100(초기 현금) - (19 * 5주) = 5 (남은 현금)
# (38 * 5주 + 5(남은 현금)) = 195
# 총 14일 확인
# 성민이는 인덱스 3개를 비교해야하므로 코드를 따로 빼는게 나을 것 같음
n = int(input())
chart = list(map(int, input().split()))
a, b = n, n
tmp_a, tmp_b = 0, 0
for i in range(14):
    tmp_a += a // chart[i]
    a %= chart[i]
    if i == 13:
        a += tmp_a * chart[i]
# 이상 준현이의 주식
# 성민이는 3일간 확인후 하락장이면 4일째부터 매수, 상승장이면 매도
for i in range(11):
    if chart[i] < chart[i + 1] < chart[i + 2]:
        b += chart[i + 3] * tmp_b
        tmp_b = 0
    elif chart[i] > chart[i + 1] > chart[i + 2]:
        tmp_b += b // chart[i + 3]
        b %= chart[i + 3]
# 마지막에 주식이 남았으면 처분해야하므로 (준현이는 이미 처분함)
b += tmp_b * chart[-1]
if a == b:
    print("SAMESAME")
elif a > b:
    print("BNP")
else:
    print("TIMING")