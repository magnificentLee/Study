import sys
from collections import Counter

t = int(sys.stdin.readline())
num = []
for _ in range(t):
    num.append(int(sys.stdin.readline()))
# 산술평균
def mean(n):
    return round(sum(n) / len(n))
# 중앙값  : (n + 1) / 2 이며 n = 5일때 3번째 값이 중앙값이다. 하지만 인덱스상 3 = 2 이므로
# 수정할 필요가 있다
def median(n):
    n.sort()
    return n[len(n) // 2]
# 범위
def scope(n):
    return max(n) - min(n)
# 최빈값
def mode(n):
    nums = Counter(n).most_common()
    if len(n) > 1:  # 1개만 있을 경우 인덱스 에러가 발생하기 때문
        if nums[0][1] == nums[1][1]:
            return nums[1][0]
        else:
            return nums[0][0]
    else:
        return nums[0][0]

print(mean(num), median(num), mode(num), scope(num), sep="\n")
