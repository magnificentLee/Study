# 범위가 굉장히 넓기 때문에 이진탐색을 해야 될 것임
# 방법1
"""
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:  # if start > end: break
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    if log >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
"""
# 방법2
# 나무의 높이가 톱날의 높이보다 높은 경우에만 나무를 가져갈 수 있다
# 따라서 그런 경우에, Sum += 나무 높이 - 톱의 높이 = tree[i] - height 로 계산
# 결과를 return
n, m = map(int, input().split())
tree = list(map(int, input().split()))
def chop(height):
    treesum = 0  # 가져갈 수 있는 나무의 총합
    for i in tree:
        if i - height > 0:
            treesum += i - height  # 총합 = 나무의 높이 - 톱의 높이
    return treesum
# 원하는 나무의 양을 target에 대입
# start, mid, end = 톱의 높이
def binarysearch(target):
    start, end = 0, max(tree)
    result = 0
    while start <= end:  # if start > end: break
        mid = (start + end) // 2
        treesum = chop(mid)
        if treesum < target:
            end = mid - 1
        elif treesum >= target:
            result = mid
            start = mid + 1
    return result

print(binarysearch(m))
# 재귀형태
"""
n, m = map(int, input().split())
tree = list(map(int ,input().split()))

def chop(height):
    treesum = 0
    for i in tree:
        if i - height > 0:
            treesum += i - height
    return treesum

def binary(target, result, start, end):
    while start <= end:  # if start > end: break
        mid = (start + end) // 2
        Sum = chop(mid)
        if Sum < target:
            return binary(target, result, start, mid - 1)
        elif Sum >= target:
            result = mid
            return binary(target, result, mid + 1, end)
    return result

start = 0
end = max(tree)
result = 0
print(binary(m, result, start, end))
"""
