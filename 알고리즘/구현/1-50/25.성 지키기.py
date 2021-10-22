# 내가 생각한 풀이
# 각 행을 반복문을 돌려 "X" 가 있으면 카운트 없으면 스킵 하는 방식
# 수정 -> 입력 받을 때 부터 확인, "X" 가 있으면 카운트 없으면 아무일 없음
# 문제를 잘못 읽음
# 각 행과 "각 열"에 최소한 한 명은 있어야 됨
# 틀린 방식
"""
n, m = map(int, input().split())
count = 0
for _ in range(n):
    guard = list(input())
    if "X" not in guard:
        count += 1
print(count)
"""
# 내가 생각한 풀이
# 각 행을 반복문을 돌려 "X" 가 있으면 카운트 없으면 스킵 하는 방식
# 수정 -> 입력 받을 때 부터 확인, "X" 가 있으면 카운트 없으면 아무일 없음
# 문제를 잘못 읽음
# 각 행과 "각 열"에 최소한 한 명은 있어야 됨

n, m = map(int, input().split())
guards = [list(input()) for _ in range(n)]

count_col = 0
count_row = 0

for i in range(n):
    if "X" not in guards[i]:
        count_col += 1
for i in range(m):
    if "X" not in [guards[j][i] for j in range(n)]:
        count_row += 1

print(max(count_col, count_row))