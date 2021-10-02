# 높이 0부터 256까지(257) 모든 경우를 따져서 최솟값을 반환하면 되는 완전탐색문제
# 최악의 경우 257 * 500 * 500 = 64250000 가지 경우를 탐색하기 때문에
# 파이썬은 제한시간을 넘겨버림
# pypy3 로 통과된 답, 파이썬으론 시간초과 발생
"""
import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)
"""
"""
풀이
높이가 0~256까지 전부 답이 될 수 있는 문제라 결국은 완전 탐색 문제라고 생각한다.
플로이드-워셜 알고리즘처럼 3중 for문으로 모든 경우의 수를 다 따져보는 것이 좋을 것 같지만 조건을 보니 시간초과가 날 것 같아 Counter를 사용해 for문을 한개 줄였다.
⇒ 시간 복잡도 : O(n^2)

* 카운터를 쓰지 않고 입력 받을때 높이별로 개수를 저장해두는 것도 좋은 방법일듯하다.

설명
완전 탐색을 진행하는데 가능한 높이가 높은 것을 답으로 한다는 지문이 있고 깍는 작업이 시간이 덜 걸리기 때문에 가장 높은 높이에서 아래로 내려가면서 확인한다.
⇒ 내려가다 중간에 가능한 높은 높이에서 멈춰주려고 했는데 까먹었다. 시도해보고 되면 추가해야지

내려가면서
높이보다 높은 블럭들을 모아서 인벤토리에 더해주고
높이보다 낮은 블럭들은 모아서 필요개수에 더해준다.
다 더해주고나면 인벤토리의 블럭수가 필요개수보다 많거나 같아야 작업을 마칠 수 있으므로 해당 조건을 만족할때만 결과에 작업시간과 높이를 추가한다.
모든 높이에 대해 탐색을 마치면 lambda를 사용해 작업시간으로 정렬하고 같은 애들은 높이순으로 재정렬해서 답을 반환한다.
"""
from sys import stdin
from collections import Counter

input = stdin.readline


def minecraft(g, b):
    gg = Counter(g)
    ret = []
    # 깍는게 시간이 더 많이 걸리니까 깍는걸 더 적게하는 높은 곳부터 시작
    # 땅의 높이가 가장 높은곳에서 낮은 곳으로
    for h in range(max(gg.keys()), -1, -1):
        gt = 0
        inventory = b
        needed = 0
        for gh, gc in gg.items():
            # 지정 높이(h)보다 높은 곳은 깍아서 인벤토리로
            if h < gh:
                inventory += (gh - h) * gc
                gt += 2 * (gh - h) * gc
            # 지정 높이(h)보다 낮은 곳은 갯수 확인
            elif h > gh:
                needed += (h - gh) * gc
                gt += (h - gh) * gc
        # 지정된 높이(h)보다 작은 곳을 채울 블록이 있는지 확인
        if inventory >= needed:
            ret.append([gt, h])
        # 없으면 한칸 내려감
    ret.sort(key= lambda x: (x[0], -x[1]))
    return ret[0]


if __name__ == "__main__":
    n, m, b = map(int, input().split())
    grounds = []
    for _ in range(n):
        grounds.extend(list(map(int, input().split())))
    res = minecraft(grounds, b)
    print(res[0], res[1])
