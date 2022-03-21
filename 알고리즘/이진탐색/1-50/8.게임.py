# 백준 1072 게임
# 푸는 방법을 도저히 몰라 블로그들을 참고함

# z는 반올림이 아니라 소수점을 버리는 것
from sys import stdin
input = stdin.readline

x, y = map(int, input().split())
z = (100 * y) // x  # 부동소수점 오차 때문에 소수 연산후 100을 곱하는게 아닌 미리 100을 곱해서 계산함 (%이기 때문)
start, end = 0, x
result = x  # 기본적인 최소 횟수는 x,
# y = x라면 (100 * x) // x 에서 공통 인수 x를 소거해주면 100이 되기 때문
# 따라서 겨로가 result와 끝값 end = x로 잡으면 됨
# 줄어들 수 없는 경우, 즉 계속 계산해봐야 100에 근접해지지만 수가 변하지 않는 경우(100을 곱했을 때 소숫점 단위에서만 움직이는 경우)
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        k = (100 * (y + mid)) // (x + mid)
        if k > z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(result)