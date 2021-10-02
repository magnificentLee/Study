# dfs bfs 문제가 아니므로 착각하지말것
"""
병든 나이트의 움직이는 경우들
1. 2칸 위로, 1칸 오른쪽
2. 1칸 위로, 2칸 오른쪽
3. 1칸 아래로, 2칸 오른쪽
4. 2칸 아래로, 1칸 오른쪽
"""
"""
from sys import stdin
n, m = map(int, stdin.readline().split())
if n == 1:  # 이동자체가 불가능
    print(1)  # 따라서 제자리만 방문처리
elif n == 2:
    print(min(4, (m + 1) // 2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m - 2)
"""
# 방문위치는 처음 시작지점을 포함함
# n = 3, m = 7 이상 일 때 모든 이동 방법을 사용해야 함
# 따라서 그보다 작을 때는 동일한 이동 방법만을 사용할 수 없기 때문에 최댓값이 4임
from sys import stdin as st
n, m = map(int, st.readline().split())
if n == 1:
    result = 1
elif n == 2:
    result = min(4, (m + 1) // 2)
else:
    if m < 7:
        result = min(4, m)
    else:
        result = m - 2
print(result)