# 5로 나누되 나눌 수 없다면 3을 빼서 진행해볼것
n = int(input())
result = 0
while n >= 0:
    if n % 5 == 0:
        result += n // 5
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)