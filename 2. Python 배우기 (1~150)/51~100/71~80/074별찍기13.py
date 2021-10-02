n = int(input())
a = n
for i in range(1, n + 1):
    print("*" * i)
for j in range(1, n):
    print("*" * (a - j))
# 출력형식이 잘못된 경우
# 별 다음으로 공백을 추가한 경우임
