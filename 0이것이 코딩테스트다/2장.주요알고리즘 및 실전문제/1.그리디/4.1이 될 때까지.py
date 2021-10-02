# 최종결과 n = 1 이라는 점에서 작성
# if 문 n % k == 0 으로 계속 확인해주기 때문에 시간복잡도에서 좋은 코드라 볼 수 없음
n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)
