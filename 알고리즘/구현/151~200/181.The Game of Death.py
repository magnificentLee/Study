# 단순 그래프 탐색 문제
# 주어지는 값이 인덱스 + 1 (실제값)이기 때문에 주의할것
# 희현이가 주경이를 걸리게 하고 싶을 때 불러야 하는 최소 숫자 K 를 구하는 문제
# 희현 = 시작, 주경 = 끝(n)

# 2052ms
def graph(idx):
    for j in array[idx]:
        if not visited[j]:
            visited[j] = visited[idx] + 1
            graph(j)


t = int(input())
for _ in range(t):
    n = int(input())
    visited = [0] * (n + 1)
    array = [0] + [[int(input())] for _ in range(n)]
    graph(1)
    if visited[n] > 0:
        print(visited[n])
    else:
        print(0)