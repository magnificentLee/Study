# 시간에 따라 패널티가 계속 누적되므로 시간이 작은것을 먼저 풀어야 패널티가 낮음

n = sorted([list(map(int, input().split())) for _ in range(11)], key=lambda x: x[0])
penalty = 0
time = 0
for i in range(11):
    time += n[i][0]  # 시간은 10, 20 + 10, 30 + 20 + 10... 같은 방식으로 늘어남, 패널티는 시간에 영향X
    penalty += time + (20 * (n[i][1]))
print(penalty)