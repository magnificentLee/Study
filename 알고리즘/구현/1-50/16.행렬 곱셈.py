# (a1 a2 a3) * (x1 y1)  = a1x1 + a2x2 + a3x3 , a1y1 + a2y2 + a3y3
#  b1 b2 b3     x2 y2     b1x1 + b2x2 + b3x3 , b1y1 + b2y2 + b3y3
#               x3 y3
# for문으로 요소 그대로 곱해서 result 리스트에 추가하는 방식은 인덱스 에러가 발생할것임
"""
3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3
"""
# 3중 for문에서 런타임 에러가 발생한듯 - 해결함
n, m = map(int, input().split())
array1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
array2 = [list(map(int, input().split())) for _ in range(m)]
result = [[0 for _ in range(k)] for _ in range(n)]  # n : 상하길이, y : 좌우길이
for i in range(n):  # 3
    for j in range(k):  # 3
        for l in range(m):  # 2
            result[i][j] += array1[i][l] * array2[l][j]
for i in result:
    print(*i)