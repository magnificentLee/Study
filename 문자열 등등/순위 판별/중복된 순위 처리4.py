# 순위중 특정 후보의 등수 뽑기
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
medal = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    medal.append(tmp)
# 메달 등급 순으로 정렬
# 람다를 사용할 경우 제일 앞이 뒤로 밀려나므로 역순으로
medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
for i in range(n):
    if medal[i][0] == k:
        idx = i
for i in range(n):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break