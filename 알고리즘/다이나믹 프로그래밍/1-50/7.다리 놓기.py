# 문제 조건을 확인
# m개의 지역에 n개의 다리를 짓는 경우의 수 = 조합
# mCn 으로 나타낼 수 있음
# mCn : 예를 들어 5C2 = 5*4/2*1 = 5*4*3*2*1/3*2*1*(2*1) 즉, 5!/3!*2!
# 요약하면 m!/(m-n)!*n!
def factorial(nums):
    result = 1
    for i in range(1, nums + 1):
        result *= i
    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    up = factorial(m)
    down1 = factorial(m - n)
    down2 = factorial(n)
    print(up // (down1 * down2))