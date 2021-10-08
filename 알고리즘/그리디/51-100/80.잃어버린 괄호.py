# 55 + 60 - 30 -> 115 - 30
# 55 - 60 + 30 -> 55 - 90 = 35
# 즉, + 기준 괄호 계산
string = input().split("-")
nums = []
for i in string:
    end = i.split("+")
    plus = 0
    for j in end:
        plus += int(j)
    nums.append(plus)
minus = nums[0]
for i in nums[1:]:
    minus -= i
print(minus)