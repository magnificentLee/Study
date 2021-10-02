# 4 6
# 19 15 10 17
n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in nums:
        if i > mid:
            total += i - mid
    if total < m:  # 잘라낸 떡의 양이 부족하면 떡을 더 많이 자르기
        end = mid - 1
    else:  # 잘라낸 떡의 양이 충분하면 떡을 덜 자르기
        result = mid  # 최대한 덜 잘라야하므로 정답 기록
        start = mid + 1
print(result)