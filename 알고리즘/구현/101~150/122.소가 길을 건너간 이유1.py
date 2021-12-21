# 각각의 소의 위치와 상태를 기록, 상태가 다르면 카운트하고 상태를 바꿔주게끔?
# 위치는 인덱스로 해결?, 1, 0 으로 visited를 시작하면 반대쪽 시작은 자동으로 카운트 되기 때문에 오답발생
# -1로 시작해서 -1이 아니면서 상태가 변할때 카운트되게?
# 관찰 횟수, 소의 마릿수가 아님
visited = [-1 for _ in range(11)]  # 소의 번호는 총 10개
result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if visited[a - 1] == -1:
        visited[a - 1] = b
    if visited[a - 1] != b:
        result += 1
        visited[a - 1] = b  # 새로운 상태 지정을 안 해줘서 틀렸음
print(result)

# 문제를 잘못봤음
# 1, 0 은 건너고 안 건너고가 아님
# 왼쪽 오른쪽에 위치해있다는 상태표시임
# 따라서 (3, 1) 이 (3, 0)으로 바뀌었다면 건넜다는것

"""
array = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    array.append((a, b))
result = 0
for i in set(array):
    if i[1] == 1:
        result += 1
print(result)
"""
