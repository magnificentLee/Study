# 4개의 값은 A팀 vs B팀, 0점 1점 이라는뜻
# 최종 수정
n = int(input())
array = [[i, 0] for i in range(n)]
for i in range((n * (n - 1)) // 2):
    a, b, x, y = list(map(int, input().split()))
    if x == y:
        array[a - 1][1] += 1
        array[b - 1][1] += 1
    elif x > y:
        array[a - 1][1] += 3
    else:
        array[b - 1][1] += 3
# 아래는 순위 판별
idx = [1] * n
for i in range(n):
    count = 0
    for j in range(n):
        if array[i][1] < array[j][1]:
            count += 1
    idx[array[i][0]] += count
for i in idx:
    print(i)
"""
n = int(input())
array = [[i, 0] for i in range(n)]
for i in range((n * (n - 1)) // 2):
    a, b, x, y = list(map(int, input().split()))
    if x == y:
        array[a - 1][1] += 1
        array[b - 1][1] += 1
    elif x > y:
        array[a - 1][1] += 3
    else:
        array[b - 1][1] += 3
array.sort(key=lambda z: z[1], reverse=True)
# 아래는 순위 판별
idx = [1] * n
for i in range(n):
    count = 0
    for j in range(n):
        if array[i][1] < array[j][1]:
            count += 1
    idx[array[i][0]] += count
for i in idx:
    print(i)
"""
# 새벽에 정신놓고 풀었던 방식, 당연히 제대로 작동하지 않음
"""
for i in range(1, n):
    if array[i - 1][1] == array[i][1]:
        idx[array[i][0]] = grade
        count += 1
    elif array[i - 1][1] != array[i][1]:
        idx[array[i][0]] = grade + count
        grade += 1
        count = 0
"""