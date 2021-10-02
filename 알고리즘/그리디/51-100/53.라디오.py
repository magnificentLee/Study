# 첫 시도 : count += 1 때문에 중복으로 더해져서 틀렸음 - 수정
"""
a, b = map(int, input().split())
n = int(input())
nums = [int(input()) for _ in range(n)]
count = 0
result = abs(a - b)
if b in nums or a == b:  # 한 번에 갈 수 있는 경우
    print(1)
else: # 한 번에 못 가는 경우
    for i in range(n):
        if abs(b - nums[i]) < result:
            count = 1  # count += 1 을 하게되면 중복으로 계속 더해지기 때문에 수정함
            result = abs(b - nums[i])
    print(result + count)
"""
# 깔끔하게 함수화
def radio_count(a, b, n, array):
    first = abs(a - b)
    result = 0
    if b in array or a == b:
        result = 1
    else:
        for i in range(n):
            if abs(b - nums[i]) < first:
                result = 1
                first = abs(b - nums[i])
        result += first
    return result


a, b = map(int, input().split())
n = int(input())
nums = [int(input()) for _ in range(n)]
print(radio_count(a, b, n, nums))


# 틀렸던 방법
"""
a, b = map(int, input().split())
n = int(input())
nums = [int(input()) for _ in range(n)]
count = 0
result = abs(a - b)
if b in nums or a == b:
    print(1)
else:
    for i in range(n):
        if abs(b - nums[i]) < result:
            result = abs(b - nums[i])
            count += 1
    print(result + count)
"""
