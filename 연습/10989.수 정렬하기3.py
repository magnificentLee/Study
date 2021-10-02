# 기존의 계수 정렬은 메모리 초과가 떴기 때문에 버블 정렬로 선회했지만 오답
"""
from sys import stdin

input = stdin.readline

def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)
def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


n = int(input())
nums = [int(input()) for _ in range(n)]
print(*merge_sort(nums), sep="\n")
"""
from sys import stdin
input = stdin.readline

n = int(input())
nums = [0] * 10001
for _ in range(n):
    nums[int(input())] += 1
for i in range(len(nums)):
    if i != 0:
        for j in range(nums[i]):
            print(i)