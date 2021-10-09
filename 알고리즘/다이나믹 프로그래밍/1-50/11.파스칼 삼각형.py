# R C W : R행 C열 길이 W의 변
r, c, w = map(int, input().split())
nums = [[1] * (i + 1) for i in range(60)]

for i in range(2, r + w):
    for j in range(1, i):
        nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
# 여기까지 기본적인 파스칼의 삼각형 구현 방식
result = 0
iter = 1
for i in range(r - 1, r + w - 1):
    for j in range(iter):
        result += nums[i][c - 1 + j]  # c - 1 + j 를 해줘야 c값을 바꿨을때 제대로 작동함
        print(nums[i][c - 1 + j])
    iter += 1
print(result)
# 틀린 방식
"""
# R C W : R행 C열 길이 W의 변
r, c, w = map(int, input().split())
nums = [[1] * (i + 1) for i in range(60)]

for i in range(2, r + w):
    for j in range(1, i):
        nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
# 여기까지 기본적인 파스칼의 삼각형 구현 방식
result = 0
for i in range(r - 1, r + w - 1):
    for j in range(c - 1, i - 1):
        result += nums[i][j]
print(result)
"""