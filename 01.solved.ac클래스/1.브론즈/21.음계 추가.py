n = list(map(int, input().split()))
nums = list(range(1, 9))
rev = sorted(nums, reverse=True)
if n == nums:
    print("ascending")
elif n == rev:
    print("descending")
else:
    print("mixed")