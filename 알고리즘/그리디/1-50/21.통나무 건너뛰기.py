# 풀이, 구현에서 난이도가 있기 때문에 실버1 문제인것 같음
# 내림차순으로 정렬시 처음과 맨끝이 만나 차이가 많이 나기 때문에 X
# 가장 큰 값을 가운데에 놓고 왼쪽 오른쪽 번갈아 놓으면 된다
# 이렇게 할 경우 오름/내림차순 정렬을 할 경우 1~2 개 정도의 차이가 나므로
# 결과적으로 최대 높이 차이는 정렬했을 때의 인덱스 두 개 정도 차이가 남
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    trees = sorted(map(int, stdin.readline().split()))
    result = 0
    for i in range(2, n):
        result = max(result, abs(trees[i] - trees[i - 2]))
    print(result)