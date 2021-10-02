# 첫 시도 : 실패
"""
t = int(input())
cows = []
result = 0
for i in range(t):
    start, end = list(map(int, input().split()))
    cows.append((start, end))
cows.sort(key=lambda x: x[0])
result += sum(cows[-2]) + cows[len(cows) - 1][1]
print(result)
"""
# 솔루션
"""
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)])

time = 0
for i in range(n):
    x, y = arr[i]
    print(time, x, y)
    if time < x:
        time = x
        print(time)
    time += y
    print(time, x, y)
print(time)
"""
# 내 방법
n = int(input())
# 리스트 생성, 도착한 순서대로 정렬
cows = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
result = 0
# 시간 최신화, 만약 가장 최근에 도착한 시간이 있으면 이전까지의 시간들은 필요 없음
for i in range(n):
    start, end = cows[i]
    if result < start:
        result = start
    result += end
print(result)