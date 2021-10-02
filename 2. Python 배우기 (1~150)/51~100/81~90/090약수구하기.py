p, q = map(int, input().split())
data = []

for i in range(1, p + 1):
    if p % i == 0:
        data.append(i)  # 어차피 1부터 순서대로 나누기 때문에 sorted 할 필요없음
if len(data) < q:
    print(0)
else:
    print(data[q - 1])  # q 번째로 작은 수
