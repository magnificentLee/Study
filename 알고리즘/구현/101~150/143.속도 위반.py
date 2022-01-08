# 위반한 횟수가 아닌 위반한 속도의 최댓값임에 주의!!
# 도로 길이를 넘기지 못했을 때 해당 도로의 남은 길이만큼 돌아야함
# 제한 속도를 넘기지 못하면 남은 길이만큼 빼서 비교해야 할 것
# 각각의 인덱스 값을 별개로 작동시켜야할것임
# 인덱스 값과 도로 값을 반복문에서 동시에 처리하려고 했는데 에러가 발생할 것으로 예상됨
# 미리 시작값을 제외한 1부터 누적값을 적용하면 리스트를 만들면 어떨까
"""
입력값이 다음과 같을 때
3 3
40 75
50 35
10 45
40 76
20 30
40 40
예상 길이 차이 : 40 - 40 = 0, 50 - 20 = 30, 30+10 - 40 = 0
누적값을 적용한 경우
[[40, 75], [90, 35], [100, 45]]
[[40, 76], [60, 30], [100, 40]]
예상과 같다는 것을 알 수 있음
"""
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
target = [list(map(int, input().split())) for _ in range(m)]
for i in range(1, n):
    array[i][0] += array[i - 1][0]
for i in range(1, m):
    target[i][0] += target[i - 1][0]
tmp, result = 0, 0
idx_array, idx_target = 0, 0


def check(x, y):
    if x < y:
        return y - x
    return 0


while True:
    if idx_array >= n and idx_target >= m:
        break

    road, move = array[idx_array][0], target[idx_target][0]
    limit, speed = array[idx_array][1], target[idx_target][1]
    tmp = check(limit, speed)
    # result = x > result and x or result (삼항연산자로 가능)
    result = max(tmp, result)

    # 인덱스를 초과하는 경우 에러가 발생하는것에 주의
    if road == move:
        idx_array += 1
        idx_target += 1
    elif road > move and idx_target < m:
        idx_target += 1
    elif road < move and idx_array < n:
        idx_array += 1
print(result)