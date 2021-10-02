# 왕복 1회만, 학교에 있는 최소 시간이므로
# 가장 늦게 등교한 사람 - 가장 먼저 하교한 사람
"""
from sys import stdin as st

t = int(st.readline())

n = [list(map(int, st.readline().split())) for _ in range(t)]

start = sorted(n, key=lambda x: x[0], reverse=True)
end = sorted(n, key=lambda x: x[1])
time = start[0][0] - end[0][1]
if time > 0:
    print(time)
else:
    print(0)
"""
# 3번 정렬을 하기 때문에 시간이 4488ms 걸림
# 따라서 다른 방법을 써서 줄여야 됨

# 왕복 1회만, 학교에 있는 최소 시간이므로
# 가장 늦게 등교한 사람 - 가장 먼저 하교한 사람
# 즉, max(등교시간) - min(하교시간)
from sys import stdin as st

t = int(st.readline())

start = []
end = []
for _ in range(t):
    i, j = map(int, st.readline().split())
    start.append(i)
    end.append(j)
s = max(start)
e = min(end)
time = s - e
if time > 0:
    print(time)
else:
    print(0)
# 해당 방법은 176ms 까지 줄일 수 있었음
