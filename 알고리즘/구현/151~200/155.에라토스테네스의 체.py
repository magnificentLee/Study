# 방문 리스트를 만들어
# 2중 리스트로 숫자의 배수들을 지워가면서 진행하는 방식? (숫자의 범위는 1천까지)
# 이전 에라토스테네스의체 연습에서 썼던 방식, 제곱근까지 확인 하는 방법으로 하면 통과할까?
# => 예제에서 오답 발생함(특정 위치:제곱근 넘어서 까지 확인해야하므로 오답이 나오는 것 같음)
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())  # 전체N, K번째 지워진 수

flag = [0] * (n + 1)
count = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if not flag[j]:  # 방문하지 않았다면
            flag[j] = 1  # 방문처리
            count += 1  # 지워진 수 카운트
            if count == k:
                print(j)
                exit()