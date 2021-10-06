# 이중 if문들, else를 제거하여 시간복잡도를 줄인 결과 정답처리됨
from sys import stdin
input = stdin.readline

n = int(input())
v = list(map(int, input().split()))
vector_max = v[-1]
for i in range(n - 1, -1, -1):
    if v[i] > vector_max:
        vector_max = v[i]
    if vector_max % v[i] != 0:
        vector_max = v[i] * ((vector_max // v[i]) + 1)
print(vector_max)

# 결과들은 나오지만 시간초과가 발생하는 방법
"""
from sys import stdin
input = stdin.readline

n = int(input())
v = list(map(int, input().split()))
vector_max = v[-1]
for i in range(n - 1, -1, -1):
    if v[i] > vector_max:
        vector_max = v[i]
    if vector_max >= max(v):
        iter = 1
        while True:
            if v[i] * iter >= vector_max:
                vector_max = v[i] * iter
                break
            else:
                iter += 1
    else:
        continue
print(vector_max)
"""
# 결과들은 나오지만 시간초과가 발생하는 방법2
"""
from sys import stdin
input = stdin.readline

n = int(input())
v = list(map(int, input().split()))
vector_max = v[-1]
for i in range(n - 1, -1, -1):
    if v[i] > vector_max:
        vector_max = v[i]
    if vector_max >= max(v):
        if vector_max % v[i] != 0:
            vector_max = v[i] * ((vector_max // v[i]) + 1)
        else:
            continue
    else:
        continue
print(vector_max)
"""