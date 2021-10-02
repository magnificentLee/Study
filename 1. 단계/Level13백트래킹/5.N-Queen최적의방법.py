# 방법1
# n = 14 일 때 3분 43초 소요
# 테스트2. n = 14 일 때 4분 51초 소요
# 19804ms 677B
"""
import datetime

start = datetime.datetime.now()

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

end = datetime.datetime.now()
print(end - start)
"""
# 방법2
# n = 14 일 때 11분48초 소요
# 채점결과 16664ms 448B
def dfs(queen, row, n):  # row = 행
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i] - queen[row]) == row - i:  # 대각선 탐색
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0] * n, 0, n)  # [0] * n 또는 [0] * (n + 1)

n = int(input())

print(solution(n))
# 방법2 - 열을 기준으로 풀기(행은 인덱스)
"""
def dfs(queen, col, n):
    count = 0
    if n == col:
        return 1
    for row in range(n):
        queen[col] = row
        for i in range(col):
            if queen[i] == queen[col]:
                break
            if abs(queen[i] - queen[col]) == col - i:
                break
        else:
            count += dfs(queen, col + 1, n)

    return count

def solution(n):
    return dfs([0] * n, 0, n)  # [0] * n 또는 [0] * (n + 1)

n = int(input())
print(solution(n))
"""