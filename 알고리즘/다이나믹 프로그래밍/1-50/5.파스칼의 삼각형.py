# 직접 나열하면서 확인
# nums[i][j] == nums[i - 1][j - 1] + nums[i - 1][j]
# 단, 마지막 번째 열은 1로 끝나므로 for문을 그 전까지만 돌리게 할 것
# [1] * (i + 1) 로 구성된 리스트를 만들어서 내부값을 최신화 및 이용하는 방식을 사용하면
# 메모리를 먹을지언정 시간복잡도는 낮을것임

n, k = map(int, input().split())

nums = [[1] * (i + 1) for i in range(31)]  # 총 30행

for i in range(2, n):
    for j in range(1, i):  # 마지막 수는 1이기 때문
        nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
print(nums[n - 1][k - 1])  # 인덱스상 0부터 시작하기 때문에 -1