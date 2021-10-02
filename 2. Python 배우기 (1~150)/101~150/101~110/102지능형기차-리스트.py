import sys

old_total = 0
max_total = 0
max_list = []
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    total = old_total + b - a
    if total > old_total:
        max_total = total
        max_list.append(max_total)
    old_total = total
print(max(max_list))
# 이전의 기차와 달리 나중에 max_total 값이 한 번 더 바뀜
# 따라서 리스트에 저장해서 맥스값을 뽑아내는게 편함
