# 현재값과 다음값들을 계속 곱하면서 비교하는 방식은 맞지 않을 것
# 현재값과 현재 * 이전값을 비교하면서 dp 리스트에 최신화 시켜주는 방식?
# but dp 리스트에 저장하면 int float 에러가 발생, 따라서 기존 리스트에 최신화 시켜주자
n = int(input())
numbers = [float(input()) for _ in range(n)]
for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i] * numbers[i - 1])
print("%.3f" % max(numbers))
