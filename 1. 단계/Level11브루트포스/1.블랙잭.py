# 라이브러리를 이용하는 방법
from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
biggest_sum = 0
for i in combinations(card, 3):
    temp_sum = sum(i)
    if biggest_sum < temp_sum <= m:
        biggest_sum = temp_sum
print(biggest_sum)
# 3중 for문을 이용하는 방법
"""
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in range(0, n - 2):  # 1 2 3 4 5가 있을 때 i 는 1~3까지 인덱스 초과가 안 되게
    for j in range(i + 1, n - 1):  # 2~4 까지 인덱스 초과가 안 되게
        for k in range(j + 1, n):  # 3~5 까지 인덱스 초과가 안 되게
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])
print(result)
"""
# 런타임에러 발생
"""
from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
result_list = []
card_perm = list(combinations(card, 3))
for i in card_perm:
    result = sum(i)
    result_list.append(result)
result_list.sort()
for i in range(len(result_list)):
    if result_list[i] == m:
        print(result_list[i])
        break
    if result_list[i] < result_list[i + 1] and result_list[i + 1] > m:
        print(result_list[i])
        break
"""