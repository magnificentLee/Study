# 일반적인 경우
"""
def bisect(a, x, lo = 0, hi = None):
    if lo < 0:
        raise ValueError("lo must be non-negative")
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
"""
# 이진탐색 모듈 bisect
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))