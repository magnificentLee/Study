import sys

score = [[int(sys.stdin.readline()), i + 1] for i in range(8)]
score = sorted(score, key=lambda x: -x[0])
score_sum = 0
answer = []
for i in range(5):
    score_sum += score[i][0]
    answer.append(score[i][1])

print(score_sum)
answer = sorted(answer)
for i in answer:
    print(i, end=" ")

# [[66, 6], [64, 8], [50, 3], [48, 4], [33, 5], [30, 2], [20, 1], [0, 7]]
# score[0][0] = 66, score[0][1] = 6
