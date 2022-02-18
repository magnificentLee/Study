n = int(input())
array = sorted([list(map(int, input().split())) for _ in range(n)])
dp = []
max_start = array[-1][0]
def dfs(idx, cur):
    cur += array[idx][2]  # point of current_time
    if array[idx][1] > max_start:  # 90 150, 110 140 일 경우 150 > 110 이므로 더 할 수 없기 때문에 바로 dp에 추가
        dp.append(cur)
    for j in range(idx + 1, n):
        if array[idx][1] > array[j][0]:
            continue
        dfs(j, cur)
for i in range(n):
    dfs(i, 0)
print(max(dp))
