# 55-50+40 -> -35 (최솟값)
# split() : split() 을 기준으로 나누는 것을 이용
front = input().split("-")
nums = []
for i in front:
    back = i.split("+")
    plus = 0
    for j in back:
        plus += int(j)
    nums.append(plus)
# 중간 결과 = 55, 90
minus = nums[0]
for i in nums[1:]:
    minus -= i
print(minus)