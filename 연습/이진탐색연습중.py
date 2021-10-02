"""
input
5
8 3 7 9 2
3
5 7 9
output
no yes yes
"""


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
m = int(input())
targets = list(map(int, input().split()))

for i in targets:
    result = binary_search(array, i, 0, n - 1)
    if result is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
"""
