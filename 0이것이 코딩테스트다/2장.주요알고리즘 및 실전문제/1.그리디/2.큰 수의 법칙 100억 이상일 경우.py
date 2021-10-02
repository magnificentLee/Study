# 무조건 시간 초과가 발생하기 때문에 수학적 아이디어가 필요하다
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1) * k)
count += m % (k + 1)  # m 이 k + 1 로 나누어 떨어지지 않는 경우

result = 0
result += count * first
result += (m - count) * second
