# 기존 코드보다 속도도 빠르고 훨씬 간결함
t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        a, b = input().split()
        a = int(a)
        li.append((a, b))
    print(li[li.index(max(li))][1])
