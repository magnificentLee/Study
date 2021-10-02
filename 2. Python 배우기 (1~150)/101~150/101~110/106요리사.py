import sys

max_score = 0
max_person = 0
for i in range(1, 6):
    score_sum = sum(list(map(int, sys.stdin.readline().split())))
    if score_sum > max_score:
        max_person = i
        max_score = score_sum
print(max_person, max_score)
