# 5
# 1 2 3 4 5
# 1 + 4 / 2 + 3 / 5 따라서 m = 5
n = int(input())
nums = sorted(map(int, input().split()))
min_val = 0
if len(nums) == 1:  # 하나만 주어진 경우
    min_val = nums[0]
elif len(nums) % 2 == 0:  # 짝수로 주어진 경우
    min_val = nums[0] + nums[-1]
    for i in range(n // 2):  # 4개의 값이 주어진 경우 0,3/1,2 로 짝 지어짐 즉, i는 절반만 필요
        if min_val < nums[i] + nums[-(i + 1)]:  # i는 0부터 시작하기 때문
            min_val = nums[i] + nums[-(i + 1)]
else:  # 홀수로 주어진 경우
    min_val = nums[-1]  # 최댓값은 정렬상 마지막
    nums.pop()  # 좌우간격을 맞춰주기 위해 마지막 제거
    for i in range(len(nums)):
        if min_val < nums[i] + nums[-(i + 1)]:
            min_val = nums[i] + nums[-(i + 1)]
print(min_val)
