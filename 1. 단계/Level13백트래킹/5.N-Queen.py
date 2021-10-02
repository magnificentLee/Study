"""
#import datetime

#start_time = datetime.datetime.now()

def nqueen(sol, n):
    global count

    if len(sol) == n:  # 퀸의 위치는 n개가 나와야됨. 리스트의 길이 = n 일 때 카운트
        count += 1
        return 0
    candidate = list(range(n))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol, n)
            sol.pop()  # 솔루션에서 빠진 부분
    else:
        return 0
count = 0
num = int(input())
for i in range(num):
    nqueen([i], num)
print(count)

#end_time = datetime.datetime.now()
#print(end_time - start_time)
# pypy3으로 제출해야 통과됨 파이썬으로 제출하면 시간초과 발생
# n = 14일 때 365596개의 결과가 나오며 3분43초의 시간이 걸림
"""
"""
import sys

sys.setrecursionlimit(5000)


def check(cur_col):
    global N
    global arr

    for i in range(0, cur_col):  # 이전에 놓은 말들과 비교.
        if abs(arr[i] - arr[cur_col]) == abs(i - cur_col):
            return False
    return True


def dfs(cur_col):
    global arr
    global N
    global ans
    global visited  # 추가됨

    if cur_col == N:
        ans += 1
        return

    for i in range(N):  # 전체 행을 순회
        if visited[i]:
            continue
        arr[cur_col] = i  # 일단 퀸을 배치하고 놓을 수 있는지 확인.
        if check(cur_col):
            visited[i] = True
            dfs(cur_col + 1)
            visited[i] = False

arr = [0] * 15
N = int(sys.stdin.readline())
ans = 0
vsitied = [False for _ in range(N)]
dfs(0)
print(ans)
"""
# 구현과정
"""
col = [2, 4, 1, 3] idx 0 1 2 3
인덱스 = 행, 리스트값 = 열로 생각하면 된다
조건1. 같은 열 체크
col[i] = i번째 행에서 퀸이 놓여있는 열의 위치
col[k] = k번째 행에서 퀸이 놓여있는 열의 위치
col[i] == col[k] 라면 유망하지 않은 것
조건2. 대각선 체크
왼쪽에 위치한 퀸과의 차이는 행의 차이와 같다 : col[i] - col[k] == i - k
오른쪽에 위한 퀸과의 차이는 행에서의 차이의 마이너스와 같다 : col[i] - col[k] == k - i
따라서 col[i] - col[k] 의 절대값으로 대각선 조건을 체크한다
이 조건으로 인해 col은 [0] * (n + 1)로 시작한다.
[0] * (n) 으로 시작하면 1번째, 2번째가 대각선 조건 체크에 들어가기 때문이며
이를 방지하기 위해 맨앞에 0을 추가한다.
"""
# n = 13일 때 2분 23초가 걸림, 결과는 시간초과 발생
"""
def check(i, col):
    global answer
    n = len(col) - 1
    if (promising(i, col)):
        if i == n:
            answer += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                check(i + 1, col)

def promising(i, col):  # 같은 열, 대각선 체크
    for k in range(1, i):
        if (col[i] == col[k]) or (abs(col[i] - col[k]) == i - k):
            return False
    return True

def solution(n):
    global answer
    answer = 0

    col = [0] * (n + 1)
    check(0, col)
    return answer

n = int(input())

print(solution(n))
"""
# n = 14 일 때 11분48초 소요
def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i] - queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0] * n, 0, n)

n = int(input())

print(solution(n))