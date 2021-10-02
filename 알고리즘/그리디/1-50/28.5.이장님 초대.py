# 모든 나무가 자란 다음날 부는 것
# 늦게 자라는 나무를 먼저 심을 것, 즉 내림차순
# 각 값 + 값의 인덱스 + 2?
t = int(input())
n = sorted(map(int, input().split()), reverse=True)
# result = [n[i] + n.index(n[i]) + 2 for i in range(len(n))] 시간초과발생
result = []
for i, j in enumerate(n):
    result.append(i + j + 2)
print(max(result))