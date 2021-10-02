"""
from itertools import permutations

n, m = map(int, input().split())
n_list = [i for i in range(1, n + 1)]
perm_list = list(permutations(n_list, m))
for i in perm_list:
    print(" ".join(map(str, i)))
"""
# 위 방법도 정답에 맞지만 단원 제목이 백트래킹인 이유를 생각하자
# DFS 혹은 BFS 로 문제를 풀라는 것
"""
n, m = map(int, input().split())
visited = [False] * n  # 탐사여부 체크
out = []  # 출력 내용
def dfs(depth, n, m):
    if depth == m:  # 탈출 조건
        print(" ".join(map(str, out)))  # list를 str으로 합쳐 출력
        # print(*out) # 으로 써도 됨
        return
    for i in range(len(visited)):  # 탐사 체크 하면서
        if not visited[i]:  # 탐사 안 했을 경우
            visited[i] = True  # 탐사시작(중복제거)
            out.append(i + 1)  # 탐사 내용
            dfs(depth + 1, n, m)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거
dfs(0, n, m)
"""
n, m = map(int, input().split())
n_list = [i + 1 for i in range(n)]  # 숫자 리스트(시작값은 1부터임)
check_number = [False] * n  # 중복숫자 체크
array = []  # 출력할 수열
def DFS(x):
    if x == m:
        print(*array)
        return
    for i in range(n):
        if check_number[i]:  # check_number == True, 중복될 경우 패스
            continue

        array.append(n_list[i])  # 수열 추가
        check_number[i] = True  # 사용한 수 체크

        DFS(x + 1)  # + 1 번째 수열을 위해 재귀함수 호출

        array.pop()  # 수열 마지막 자리 삭제
        check_number[i] = False  # 사용한 수 초기화
DFS(0)
