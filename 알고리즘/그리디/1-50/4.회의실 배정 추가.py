from sys import stdin as st

n = int(st.readline())
time = [list(map(int, st.readline().split())) for _ in range(n)]
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
last = 0
result = 0
for i, j in time:
    if i >= last:
        result += 1
        last = j
print(result)