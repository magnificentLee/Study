# 딕셔너리 이용
n, m, k = map(int, input().split())

cands = {}
for i in range(n):
    cands[i + 1] = 0

for i in range(m):
    scores = list(map(float, input().split()))
    for j in range(0, 2 * n, 2):
        if scores[j + 1] > cands[scores[j]]:
            cands[scores[j]] = scores[j + 1]
total = sorted(cands.values(), reverse=True)
result = sum(total[:k])
print("%0.1f" % result)
