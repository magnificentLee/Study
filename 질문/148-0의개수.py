import sys

t = int(input())
for i in range(t):
    count = 0  # count 위치가 입력 밑으로 위치할 경우 틀림, 이유는 모르겠다.
    a, b = map(int, sys.stdin.readline().split())
    for j in range(a, b + 1):
        c = str(j)
        count += c.count("0")
    print(count)
"""
a, b = map(int, input().split()) : 3404ms, 182B
a, b = map(int, sys.stdin.readline().split()) : 3408ms, 207B
어째서 속도가 더 느리게 나오는지 이유를 모르겠음
"""