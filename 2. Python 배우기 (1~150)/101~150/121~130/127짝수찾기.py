import sys

t = int(input())

for i in range(t):
    n_list = list(map(int, sys.stdin.readline().split()))
    e_list = []
    for j in n_list:
        if j % 2 == 0:
            e_list.append(j)
    print(sum(e_list), min(e_list))
# if j % 2 == 1: , n_list.remove[j] = 실패
# 기존 리스트에서 완전히 제거하는게 잘못된 방법인 것 같다
# 결과값은 같지만 출제 의도와는 다른것으로 판단됨

"""테스트
import sys

n_list = list(map(int, sys.stdin.readline().split()))
print(n_list)
for i in n_list:
    if i % 2 == 1:
        n_list.remove(i)
print(n_list)
"""