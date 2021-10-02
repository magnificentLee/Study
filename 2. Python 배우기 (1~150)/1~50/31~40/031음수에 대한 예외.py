k, n, m = map(int, input().split()) # 과자 가격, 개수, 현재 가진 돈

total = k * n - m  # 20 10 320 일 경우 -120이 나오기 때문에
if total < 0:  # 음수가 나오는 경우를 위한 예외
    total = 0

print(total)
"""
k, n, m = map(int, input().split())
answer = k * n - m
if answer > 0:
    print(answer)
else:
    print(0)
"""