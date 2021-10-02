# 76ms / 225B
n = int(input())
score_list = list(map(int, input().split()))
score_list = sorted(score_list)
total = 0
for i in score_list:
    new_score = i / max(score_list) * 100
    total += new_score
avg = total / n
print("%.2f" % avg)
""" 72ms / 263B
n = int(input())
score_list = list(map(int, input().split()))
score_list = sorted(score_list)
new_score_list = []
for i in score_list:
    new_score = i / max(score_list) * 100
    new_score_list.append(new_score)
avg = sum(new_score_list) / n
print("%.2f" % avg)
매 반복마다 더해주는 것 보다 리스트에 저장한 뒤 한번에 더해주는게 더 빠름
"""