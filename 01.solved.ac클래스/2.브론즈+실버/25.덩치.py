t = int(input())
n = []
for _ in range(t):
    a, b = map(int, input().split())
    n.append((a, b))
for i in n:
    result = 1
    for j in n:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    print(result, end=" ")