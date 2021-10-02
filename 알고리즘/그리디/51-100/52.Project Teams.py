# 수의 범위가 넓지 않다는 점
# 팀 수 = n, 학생의 수 = 2 * n, 즉 학생의 수가 홀수 일 때를 고려하지 않아도 된다는 점에서 작성
n = int(input())
nums = sorted(map(int, input().split()))
result = nums[-1] + nums[0]
for i in range(n):
    if result > nums[-(i + 1)] + nums[i]:
        result = nums[-(i + 1)] + nums[i]
print(result)