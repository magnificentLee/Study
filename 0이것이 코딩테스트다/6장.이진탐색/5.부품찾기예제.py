"""
input
n = 5
[8, 3, 7, 9, 2]
m = 3
[5, 7, 9]
"""
"""
output
no yes yes
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))
t = int(input())
target = list(map(int, input().split()))
for i in target:
    if binary_search(array, i, 0, n - 1) is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")