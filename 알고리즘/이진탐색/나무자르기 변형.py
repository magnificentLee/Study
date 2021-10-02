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