# 백준 2776 암기왕
# 이진탐색(재귀함수가 아닌 반복문을 이용한) 풀이가 있지만 훨씬 오래걸림

# 집합을 이용한 다른 방법(stdout을 추가해줬음)
# 214724KB, 1264ms, 303B
from sys import stdin, stdout
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = set(map(int, input().split()))
    m = int(input())
    data = list(map(int, input().split()))
    for i in data:
        stdout.write("1\n") if i in array else stdout.write("0\n")